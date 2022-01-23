<template>
  <div class="sync">
    <template v-if="$store.state.isAuthenticated">
        <div class="columns">
          <div class="column is-2 is-offset-1 pt-4 is-offset-1-mobile">
            <h1 class="has-text-success">My Synced Channels</h1>
          </div>
        </div>
        <div class="columns">
          <div
            class="column is-1 is-offset-1 is-10-mobile
            is-offset-1-mobile"
            v-for="channel in my_synced_channels"
            v-bind:key="channel.channel_id"
          >
            <a :href="channel.channel_url" target="_blank">
            <div class="has-text-centered">
              <figure class="image is-128x128 is-inline-block">
                  <img class="is-rounded" :src="channel.channel_logo"/>
              </figure>
              <p>{{ channel.channel_name }}</p>
            </div>
            </a>
          </div>
        </div>
        <div class="columns">
            <div class="column is-4 is-offset-4 py-6">
                <form class="box" @submit.prevent="submitForm">
                    <div class="field">
                        <label>Channel to sync:</label>
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
                        <div class="control has-text-centered">
                            <button class="button is-primary is-fullwidth">Sync</button>
                            <p class="is-size-7">This may take a few seconds.</p>
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
      my_synced_channels: [],
    };
  },
  mounted() {
    this.getSyncedChannels();
  },
  methods: {
    submitForm(e) {
      const formdata = {
        channel_url: this.channel,
      };
      axios
        .post('api/v1/sync/', formdata)
        .then((response) => {
          this.my_synced_channels = [];
          this.getSyncedChannels();
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
    getSyncedChannels() {
      axios
        .get('api/v1/sync/')
        .then((response) => {
          if (response.data) {
            for (let i = 0; i < response.data[0].channels.length; i += 1) {
              this.my_synced_channels.push(response.data[0].channels[i]);
            }
          }
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
