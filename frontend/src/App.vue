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
            <!-- <button class="button is-inverted is-dark is-fullwidth
            logout-menu is-hidden-desktop" @click="logUserOut()">
              Logout
            </button> -->
            <a href="#" class="button is-dark is-inverted is-fullwidth is-hidden-desktop" @click="signOut()">
              Logout
            </a>
            <!-- end: This only displays on mobile and tablet -->

            <!-- start: This only display on desktop. Drop down for ading new things -->
            <div class="navbar-item is-hidden-touch">
              <div class="navbar-item has-dropdown desktop-navigation is-hoverable">
                <a class="navbar-link">+</a>
                <div class="navbar-dropdown is-right">
                  <router-link to="/sync" class="navbar-item">Sync new channel</router-link>
                  <router-link to="/" class="navbar-item">Generate inspiration</router-link>
                  <router-link to="/play" class="navbar-item">Play</router-link>
                  <router-link to="/collection" class="navbar-item">My collection</router-link>
                </div>
              </div>
            </div>
            <!-- end: This only display on desktop. Drop down for ading new things -->

            <!-- start: This only display on desktop. Main drop down menu for pc users -->
            <div class="navbar-item is-hidden-touch">
              <div class="navbar-item has-dropdown is-hoverable desktop-navigation">
                <a class="navbar-link">
                  Menu
                </a>
                <div class="navbar-dropdown is-right">
                  <router-link class="navbar-item" to="/">
                    Signed in as<strong>&nbsp;{{username }}</strong>
                  </router-link>
                  <a href="#" class="button is-danger is-inverted is-fullwidth" @click="signOut()">
                    Logout
                  </a>
                </div>
              </div>
            </div>
            <!-- end: This only display on desktop. Main drop down menu for pc users -->
          </template>
          <!-- end: navbar if user is signed in -->

          <!-- start: navbar if user is signed out -->
          <template v-else>
            <router-link to="/" class="navbar-item has-text-success">Home</router-link>
            <router-link to="/about" class="navbar-item has-text-success">About</router-link>
            <router-link to="/how" class="navbar-item has-text-success">
              How it works!
            </router-link>
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
    // if (this.$store.state.token) {
    //   axios.defaults.headers.common['Authorization'] = `Token ${this.$store.state.token}`;
    // } else {
    //   axios.defaults.headers.common['Authorization'] = '';
    // }

    if (this.$store.state.access_token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${this.$store.state.access_token}`;
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
    this.onLoad();
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
          .get('/api/v1/me')
          .then((response) => {
            if (response && response.data[0].isPremium) {
              this.$store.state.isPremium = response.data[0].isPremium;
            } else {
              this.$store.state.isPremium = false;
            }
            this.username = response.data[0].user.username;
            if (this.username !== this.$store.state.activeUser) {
              this.$store.state.activeUser = response.data.username;
            }
          })
          .catch((error) => {
            console.log(JSON.stringify(error));
          });
      }
    },
    getRefreshToken() {
      axios
        .post('/auth/token', {
          grant_type: 'refresh_token',
          refresh_token: this.$store.state.refresh_token,
          backend: 'google-oauth2',
          client_id: 'wdGmY8cErFJxLG3aOMtksRghRklzeE9dHC13x5US',
          client_secret: 'ZfbCBer3namUYKSoiQ6MZymDwYfpGOV366EsKhXSRWPxDHmbOfGIpdOh5y4O8IIrQ5WfTX0azbg4qmwwhRIzJNgNz30LMry1FQdpjKGKy3ZaK5Z6VFwODUBZ4OTwjLsm',
          })
        .then((response) => {
          console.log(response);
          this.$store.state.access_token = response.data.access_token;
          this.$store.state.refresh_token = response.data.refresh_token;

          localStorage.setItem('access_token', this.$store.state.access_token);
          localStorage.setItem('refresh_token', this.$store.state.refresh_token);

          axios.defaults.headers.common['Authorization'] = `Bearer ${this.$store.state.access_token}`;
          // this.$router.push({ path: '/' });
          
        });
    },
    signOut() {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        console.log('User signed out.');
      });
      this.$store.state.isAuthenticated = false;
      localStorage.setItem('access_token', '');
      localStorage.setItem('refresh_token', '');
      this.$store.state.access_token = '';
      this.$store.state.refresh_token = '';
    },
    onLoad() {
      gapi.load('auth2', function() {
        gapi.auth2.init();
      });
    }
  },
  watch: {
    $route(to, from) {
      this.getMe();
      document.title = to.meta.title || 'Vig';
    },
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
