<template>
  <div class="home">
    <template v-if="$store.state.isAuthenticated">
        <div class="columns">
          <div class="column is-2 is-offset-1 py-5">
            <router-link to="/sync" class="button is-link">+ Sync more channels</router-link>
          </div>
        </div>
        <div class="columns">
          <div class="column is-10 is-offset-1 pb-4">
            <p class="is-size-5 has-text-success">Generator options:</p>
          </div>
        </div>
        <div class="columns">
          <div class="column is-1 is-offset-1 pb-0 mr-5">
            <span class="has-text-success">From:</span>
          </div>
          <div class="column is-1 pb-0 mb-0">
            <span class="has-text-success">Quantity:</span>
          </div>
        </div>
        <div class="columns">
          <div class="column is-1 is-offset-1 mr-5">
            <select v-model="generate_from">
              <option v-for="generator_option in generate_from_options"
              :key="generator_option.value" :value="generator_option.value">
                {{ generator_option.text }}
              </option>
            </select>
          </div>
          <div class="column is-1 mr-5">
            <select v-model="video_quantity">
              <option v-for="quantity in video_quantity_options"
              :key="quantity.value" :value="quantity.value">
                {{ quantity.text }}
              </option>
            </select>
          </div>
        </div>
        <div class="columns is-multiline is-centered">
            <div class="column is-8-desktop is-10-tablet
            is-offset-1-tablet is-12-mobile py-6">
                <form @submit.prevent="submitForm">
                    <div class="notification" v-if="errors.length">
                        <p
                            v-for="error in erros"
                            v-bind:key="error"
                        >
                            {{ error }}
                        </p>
                    </div>
                    <div class="columns is-centered is-multiline">
                      <div
                        class="column is-6-desktop is-one-third-tablet is-10-mobile
                        is-offset-1-mobile"
                        v-for="video in video_detail"
                        v-bind:key="video.id"
                      >
                        <a target="_blank" :href="`https://www.youtube.com/watch?v=${video.youtube_video_id}`">
                        <div class="box has-background-link media-center video-detail-box">
                          <figure class="image image is-16by9">
                            <img :src="video.thumbnail_url" alt="thumbnail">
                          </figure>
                          <br>
                          <div class="box video-detail-box has-background-link-light">
                            <h1>{{ video.title }}</h1>
                            <p class="has-text-right is-size-7">
                              <strong>{{ video.view_count }}</strong>
                            </p>
                          </div>
                        </div>
                        </a>
                      </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-fullwidth is-success">
                              Generate Inspiration
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </template>

    <template v-else>
        <div class="columns">
            <div class="column is-3-desktop is-10-tablet is-offset-4-desktop
            is-offset-1-tablet is-12-mobile py-6">
                <form @submit.prevent="submitForm">
                    <div class="notification" v-if="errors.length">
                        <p
                            v-for="error in erros"
                            v-bind:key="error"
                        >
                            {{ error }}
                        </p>
                    </div>
                    <div class="columns is-multiline-mobile is-centered">
                      <div
                        class="column is-12-desktop is-one-third-tablet is-10-mobile
                        is-offset-1-mobile"
                        v-for="video in video_detail"
                        v-bind:key="video.id"
                      >
                        <a target="_blank" :href="`https://www.youtube.com/watch?v=${video.youtube_video_id}`">
                        <div class="box has-background-link media-center video-detail-box">
                          <figure class="image image is-16by9">
                            <img :src="video.thumbnail_url" alt="thumbnail">
                          </figure>
                          <br>
                          <div class="box video-detail-box has-background-link-light">
                            <h1>{{ video.title }}</h1>
                            <p class="has-text-right is-size-7">
                              <strong>{{ video.view_count }}</strong>
                            </p>
                          </div>
                        </div>
                        </a>
                      </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-fullwidth is-success">
                              Generate Inspiration
                            </button>
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
      errors: [],
      video_detail: [],
      generate_from: 'SYNCED',
      video_quantity: 'TWO',
      generate_from_options: [
        { text: 'synced channels', value: 'SYNCED' },
        { text: 'random channels', value: 'RANDOM' },
        { text: '1 random. 1 synced', value: 'RAN_SYNC' },
      ],
      video_quantity_options: [
        { text: '1', value: 'ONE' },
        { text: '2', value: 'TWO' },
        { text: '3', value: 'THREE' },
        { text: '4', value: 'FOUR' },
      ],
    };
  },
  mounted() {
    this.submitForm();
  },
  methods: {
    submitForm(e) {
      axios
        .get('api/v1/generator/')
        .then((response) => {
          if (response.data) {
            this.video_detail = [];
            for (let i = 0; i < response.data.length; i += 1) {
              this.video_detail.push(response.data[i]);
              this.video_detail[i].view_count = this.video_detail[i].view_count.toLocaleString();
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
