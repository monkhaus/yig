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
              is-small px-2 has-text-centered is-rounded"
              @click.prevent="desync(channel.id, channel)">
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
                    <div class="field">
                        <div class="control has-text-centered">
                            <template v-if="this.syncing === true">
                              <button class="button is-primary is-fullwidth is-loading">
                                Sync
                              </button>
                            </template>
                            <template v-else>
                              <button class="button is-primary is-fullwidth">Sync</button>
                            </template>
                              <p class="is-size-7 has-text-danger">
                                <srong>
                                  Channels with thousands of videos may take a few minutes!
                                </srong>
                              </p>
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
      syncing: false,
      channel_input_box: '',
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
      this.syncing = true;
      this.channel = '';
      axios
        .post('api/v1/sync/', formdata)
        .then((response) => {
          this.my_synced_channels = [];
          this.getSyncedChannels();
          this.syncing = false;
        })
        .catch((error) => {
          if (error.response) {
            this.syncing = false;
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
      this.my_synced_channels = [];
      axios
        .get('api/v1/sync/')
        .then((response) => {
          if (response.data) {
            for (let i = 0; i < response.data[0].channels.length; i += 1) {
              this.my_synced_channels.push(response.data[0].channels[i]);
            }
            this.syncing = false;
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
    desync(id, channel) {
      axios
        .delete(`api/v1/sync/${id}`)
        .then((response) => {
          this.getSyncedChannels();
        })
        .catch((error) => {
          // catch error
        });
    },
  },
};
</script>

<style lang="scss">
@import 'mystyles.scss';
</style>
