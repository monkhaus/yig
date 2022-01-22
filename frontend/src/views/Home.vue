<template>
  <div class="home">
    <template v-if="$store.state.isAuthenticated">
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
