<template>
  <div class="sync">
    <template v-if="$store.state.isAuthenticated">
        <div class="columns">
            <div class="column is-4 is-offset-4">

                <form class="box" @submit.prevent="submitForm">
                    <div class="field">
                        <label>Channel</label>
                        <div class="control">
                            <input type="text" name="channel" class="input" v-model="channel">
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
                            <button class="button is-primary is-fullwidth">Sync</button>
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
  name: 'Sync',
  data() {
    return {
      errors: [],
      channel: '',
    };
  },
  methods: {
    submitForm(e) {
      const formdata = {
        channel_url: this.channel,
      };
      axios
        .get('api/v1/sync/')
        .then((response) => {
          console.log(response);
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

<style lang="scss">
@import 'mystyles.scss';
</style>
