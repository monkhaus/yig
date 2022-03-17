<template>
  <div class="about">
    <div class="columns is-centered py-6">
      <div class="column is-12">
        <div class="columns is-centered">
          <div class="column is-8">
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                  </div>
                  <div class="media-content">
                    <div class="media">
                        <strong>Payment successful. -></strong>&nbsp;start by&nbsp;<router-link to='/sync'>syncing a channel</router-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">

export default {
  name: 'Success',
  data() {
    return {
      errors: [],
    };
  },
  methods: {

  },
};
</script>

<style lang="scss">
@import 'mystyles.scss';
.twitter-link:hover {
  text-decoration: underline;
}
</style>
