<template>
    <div class="page-signup">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <form  class="box" @submit.prevent="submitForm">
                    <div class="field">
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
                            <button class="button is-fullwidth is-success">Sign up</button>
                        </div>
                    </div>
                    <div id="sign-up-form"></div>
                    <div class="buttons is-centered">
                        <router-link to="/log-in" class="button is-primary">Log in</router-link>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignUp',
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
