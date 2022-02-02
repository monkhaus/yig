<template>
  <div class="home py-3">
    <template v-if="$store.state.isAuthenticated">
        <div class="columns is-centered">
          <div class="column is-9-fullhd is-10-desktop is-10-tablet is-10-mobile
          has-text-centered-mobile py-5 is-offset-1-mobile">
           <h1 class="has-text-success">My collection</h1>
          </div>
        </div>
        <form @submit.prevent="submitForm" class="has-background-info">
        <div class="columns is-multiline is-centered is-mobile">
            <div class="column is-9-fullhd is-10-widescreen is-12-desktop is-10-tablet
            is-11-mobile py-6">
                    <div class="notification" v-if="errors.length">
                        <p v-for="error in erros" v-bind:key="error">
                          {{ error }}
                        </p>
                    </div>
                    <div class="columns is-multiline">
                      <div
                        class="column is-3-desktop is-6-tablet is-10-mobile is-offset-1-mobile"
                        v-for="video in video_detail"
                        v-bind:key="video.id"
                      >
                      <button class="button is-danger is-light is-small mb-1"
                      @click.prevent="removeFromCollection(video.id, video)">
                        - Remove from collection
                      </button>

                        <a target="_blank" :href="`https://www.youtube.com/watch?v=${video.youtube_video_id}`">
                        <div class="box has-background-link media-center
                        video-detail-box-collection">
                          <figure class="image is-16by9">
                            <img :src="video.thumbnail_url" alt="thumbnail">
                          </figure>
                          <br>
                          <div class="box has-background-link-light">
                            <h1>{{ video.title }}</h1>
                            <p class="has-text-right is-size-7">
                              <strong>{{ video.view_count }}</strong>
                            </p>
                          </div>
                        </div>
                        </a>
                      </div>
                    </div>
            </div>
        </div>
        </form>
    </template>

    <template v-else>
        <div class="columns">
            <div class="column is-3-fullhd is-3-desktop is-10-tablet is-offset-4-desktop
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
                        <div class="box has-background-link media-center">
                          <figure class="image is-16by9">
                            <img :src="video.thumbnail_url" alt="thumbnail">
                          </figure>
                          <br>
                          <div class="box has-background-link-light">
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
  name: 'Collection',
  data() {
    return {
      errors: [],
      video_detail: [],
      generate_from: 'SYNCED',
    };
  },
  mounted() {
    this.submitForm();
  },
  methods: {
    submitForm(e) {
      axios
        .get('api/v1/video/')
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
    removeFromCollection(id, video) {
      axios
        .delete(`api/v1/video/${id}`)
        .then((response) => {
          const index = this.video_detail.indexOf(video);
          if (index > -1) {
            this.video_detail.splice(index, 1); // 2nd parameter means remove one item only
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
.video-detail-box-collection {
  height: 90%;
}
</style>
