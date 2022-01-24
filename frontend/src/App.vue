<template>
  <div id="wrapper">

    <nav class="navbar is-primary">
      <div class="navbar-brand">
        <template v-if="$store.state.isAuthenticated">
          <router-link to="/" class="navbar-item has-text-success">
              <strong>Video Idea Generator</strong>
          </router-link>
        </template>
        <template v-else>
          <router-link to="/" class="navbar-item has-text-success">
              <strong>Video Idea Generator</strong>
          </router-link>
        </template>
        <a role="button" class="navbar-burger desktop-navigation"
        data-target="navMenu" aria-label="menu" aria-expanded="false">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navMenu">
        <div class="navbar-end">
          <!-- start: navbar if user is signed in -->
          <template v-if="$store.state.isAuthenticated">

            <!-- start: This only displays on mobile and tablet -->
            <router-link class="navbar-item is-hidden-desktop" to="/">
              Signed in as<strong>&nbsp;{{username }}</strong>
            </router-link>
            <hr class="navbar-divider logout-burger-divider">
            <button class="button is-inverted is-dark is-fullwidth
            logout-menu is-hidden-desktop" @click="logUserOut()">
              Logout
            </button>
            <!-- end: This only displays on mobile and tablet -->

            <!-- start: This only display on desktop. Drop down for ading new things -->
            <div class="navbar-item is-hidden-touch">
              <div class="navbar-item has-dropdown desktop-navigation is-hoverable">
                <a class="navbar-link">+</a>
                <div class="navbar-dropdown is-right">
                  <router-link to="/sync" class="navbar-item">Sync new channel</router-link>
                  <router-link to="/" class="navbar-item">Generate inspiration</router-link>
                </div>
              </div>
            </div>
            <!-- end: This only display on desktop. Drop down for ading new things -->

            <!-- start: This only display on desktop. Main drop down menu for pc users -->
            <div class="navbar-item is-hidden-touch">
              <div class="navbar-item has-dropdown is-hoverable desktop-navigation">
                <a class="navbar-link">
                  {{ username }}
                </a>
                <div class="navbar-dropdown is-right">
                  <router-link class="navbar-item" to="/">
                    Signed in as<strong>&nbsp;{{username }}</strong>
                  </router-link>
                  <button class="button is-danger is-inverted is-fullwidth" @click="logUserOut()">
                    Logout
                  </button>
                </div>
              </div>
            </div>
            <!-- end: This only display on desktop. Main drop down menu for pc users -->
          </template>
          <!-- end: navbar if user is signed in -->

          <!-- start: navbar if user is signed out -->
          <template v-else>
            <router-link to="/" class="navbar-item has-text-success">Home</router-link>
            <div class="navbar-item is-hidden-touch">
              <div class="buttons">
                <router-link to="/log-in" class="button is-medium is-link">
                  Log in
                </router-link>
              </div>
            </div>

            <div class="is-hidden-desktop">
              <router-link to="/sign-up" class="navbar-item">Sign up</router-link>
              <router-link to="/log-in" class="navbar-item">Log in</router-link>
            </div>
          </template>
          <!-- start: navbar if user is signed out -->
        </div>
      </div>
    </nav>

    <section id="home-section" class="section">
       <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">VideoIdeaGenerator &copy; 2021</p>
    </footer>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore');

    if (this.$store.state.token) {
      axios.defaults.headers.common['Authorization'] = `Token ${this.$store.state.token}`;
    } else {
      axios.defaults.headers.common['Authorization'] = '';
    }
  },
  data() {
    return {
      errors: [],
      username: '',
    };
  },
  mounted() {
    this.desktopNavigation();
  },
  methods: {
    desktopNavigation() {
      document.addEventListener('DOMContentLoaded', () => {
        // Get all "navbar-burger" elements
        const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

        // Check if there are any navbar burgers
        if ($navbarBurgers.length > 0) {
          // Add a click event on each of them
          $navbarBurgers.forEach((el) => {
            el.addEventListener('click', () => {
              // Get the target from the "data-target" attribute
              const { target } = el.dataset;
              const $target = document.getElementById(target);

              // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
              el.classList.toggle('is-active');
              $target.classList.toggle('is-active');
            });
          });
        }
      });
    },
    logUserOut() {
      axios
        .post('api/v1/token/logout/')
        .then((response) => {
          this.$store.commit('removeToken');
          localStorage.removeItem('token');
          this.$router.push('/log-in');
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              if (error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`);
              }
            }
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            console.log(JSON.stringify(error.message));
          } else {
            console.log(JSON.stringify(error));
          }
        });
    },
    getMe() {
      if (this.$store.state.isAuthenticated) {
        axios
          .get('/api/v1/users/me')
          .then((response) => {
            this.username = response.data.username;
            if (this.username !== this.$store.state.activeUser) {
              this.$store.state.activeUser = response.data.username;
            }
          })
          .catch((error) => {
            console.log(JSON.stringify(error));
          });
      }
    },
  },
  watch: {
    $route(to, from) {
      this.getMe();
      document.title = to.meta.title || 'Vig';
    },
    immediate: true,
  },
};
</script>

<style lang="scss">
@import 'mystyles.scss';

html, body {
  width: 100%;
  padding: 0px;
  margin: 0px;
  height: 100%;
}

body {
  background-color: $info;
}

#home-section {
  padding: 0px;
}

.logout-menu {
  justify-content: left;
  padding: 0.5rem 0.75rem;
}

.logout-burger-divider {
  display: block;
}
</style>
