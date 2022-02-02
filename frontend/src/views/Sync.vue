<template>
  <div class="sync">
    <template v-if="$store.state.isAuthenticated">
        <div class="columns">
          <div class="column is-2 is-offset-1 py-5 pr-0 mr-0">
            <router-link to="/" class="button is-link">-> Generate inspiration</router-link>
          </div>
          <div class="column is-1 py-5 ml-0">
            <button class="button is-link is-light"
            @click.prevent="toggleEditMode">Toggle edit mode</button>
          </div>
        </div>
        <div class="columns is-multiline py-2">
          <div
            class="column is-3 is-10-mobile
            is-offset-1-mobile is-hidden-mobile"
            v-for="channel in my_synced_channels"
            v-bind:key="channel.channel_id"
          >
            <template v-if="edit_mode === true">
            <div class="has-text-centered pb-1">
              <a class="button is-link is-focused
              is-small px-2 has-text-centered is-rounded">
                &#10006;
              </a>
            </div>
            </template>

            <a :href="channel.channel_url" target="_blank">
            <div class="has-text-centered">
              <figure class="image is-128x128 is-inline-block">
                  <img class="is-rounded" :src="channel.channel_logo"/>
              </figure>
              <p class="has-text-warning">{{ channel.channel_name }}</p>
            </div>
            </a>
          </div>
        </div>
        <div class="columns">
            <div class="column is-5 is-offset-4 py-6">
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
      edit_mode: false,
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
    toggleEditMode() {
      this.edit_mode = !this.edit_mode;
      console.log(this.edit_mode);
    },
  },
};
</script>

<style lang="scss">
@import 'mystyles.scss';
</style>
