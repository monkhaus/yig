<template>
  <div class="home">
    <h1>Welcome to the video idea generator.</h1>
    <template v-if="$store.state.isAuthenticated">
    You are signed in.
    </template>

    <template v-else>
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <form  class="box" @submit.prevent="submitForm">
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
                            <button class="button is-fullwidth is-success">Generate</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GenerateHomeView',
  data() {
    return {
      username: '',
      password: '',
      errors: [],
    };
  },
  methods: {
    submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password,
      };
      axios
        .post('api/v1/users/', formData)
        .then((response) => {
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
  },
};
</script>

<style>
#sign-up-form {
    border-bottom: 1px solid #dadde1;
    margin: 15px 10px;
    padding: 15px 10px;
}
</style>
