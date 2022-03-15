<template>
    <div class="page-login">
        <div class="columns">
            <div class="column is-4 is-offset-4 my-6">
                <form class="box has-background-light" @submit.prevent="submitForm">
                    <div class="field">
                        <label><strong>+ Synchronise your favourite YouTube channels</strong></label>
                    </div>
                    <div class="field">
                        <label><strong>+ Get Inspiration for your own YouTube videos.</strong></label>
                    </div>
                    <div class="field">
                        <label><strong>+ Save the videos that inspire you.</strong></label>
                    </div>
                    <div class="field">
                        <label><strong>+ Get an intuitive understanding of good thumbnails via the mini game.</strong></label>
                    </div>  
                    <!-- <div class="field">
                        <label>E-mail</label>
                        <div class="control">
                            <input type="email" name="username" class="input" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p
                            v-for="error in erros"
                            v-bind:key="error"
                        >
                            {{ error }}
                        </p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-primary is-fullwidth">Log in</button>
                        </div>
                    </div> -->
                    <div id="sign-up-form"></div>
                    <div class="buttons is-centered">
                        <!-- <router-link to="/sign-up" class="button is-centered is-success mgh-small">
                            Create New Account
                        </router-link> -->
                    <div id="google-signin-btn"></div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: [],
    }
  },
  mounted() {
    gapi.signin2.render('google-signin-btn', { // this is the button "id"
      onsuccess: this.onSignIn, // note, no "()" here
      theme: 'light',
      width: 240,
      height: 50,
    })
  },
  methods: {
    submitForm(e) {
      axios.defaults.headers.common['Authorization'] = '';
      localStorage.removeItem('token');
      const formData = {
        username: this.username,
        password: this.password,
      };
      axios
        .post('api/v1/token/login/', formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit('setToken', token);
          axios.defaults.headers.common['Authorization'] = `Token ${token}`;
          localStorage.setItem('token', token);
          this.$router.push({ path: '/' });
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
    submitGoogleForm(access_token) {
      axios.defaults.headers.common['Authorization'] = '';
      axios
        .post('auth/convert-token', {
          token: access_token,
          grant_type: 'convert_token',
          backend: 'google-oauth2',
          client_id: 'wdGmY8cErFJxLG3aOMtksRghRklzeE9dHC13x5US',
          client_secret: 'ZfbCBer3namUYKSoiQ6MZymDwYfpGOV366EsKhXSRWPxDHmbOfGIpdOh5y4O8IIrQ5WfTX0azbg4qmwwhRIzJNgNz30LMry1FQdpjKGKy3ZaK5Z6VFwODUBZ4OTwjLsm',
          })
        .then((response) => {
          this.$store.state.access_token = response.data.access_token;
          this.$store.state.refresh_token = response.data.refresh_token;
          localStorage.setItem('access_token', this.$store.state.access_token);
          localStorage.setItem('refresh_token', this.$store.state.refresh_token);

          axios.defaults.headers.common['Authorization'] = `Bearer ${this.$store.state.access_token}`;
          this.$router.push({ path: '/' });
        });
    },
    onSignIn(googleUser) {
      var profile = googleUser.getBasicProfile();
      var access_token = googleUser.getAuthResponse(true).access_token;
      // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
      // console.log('Name: ' + profile.getName());
      // console.log('Image URL: ' + profile.getImageUrl());
      // console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.

      this.submitGoogleForm(access_token);
    },
  },
};
</script>

<style>
#sign-up-form {
    border-bottom: 1px solid #dadde1;
    margin: 10px 10px;
    padding: 5px 10px;
}
</style>
