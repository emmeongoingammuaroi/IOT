<template>
  <div>
    <div class="row">
      <div class="col-md-6" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category"></h5>
            <h3 class="card-title">
              <i class="tim-icons icon-spaceship text-primary "></i>
              <router-link :to="{ name: 'livingroom' }">{{
                $t("sidebar.livingroom")
              }}</router-link>
            </h3>
          </template>
          <div class="chart-area">
            <img :src="require('@/assets/images/room1.png')" />
          </div>
        </card>
      </div>
      <div class="col-md-6" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category"></h5>
            <h3 class="card-title">
              <i class="tim-icons icon-shape-star text-primary "></i>
              <router-link :to="{ name: 'kitchen' }">
                {{ $t("sidebar.kitchen") }}
              </router-link>
            </h3>
          </template>
          <div class="chart-area">
            <img :src="require('@/assets/images/room2.jpg')" />
          </div>
        </card>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category"></h5>
            <h3 class="card-title">
              <i class="tim-icons icon-app text-primary "></i>
              <router-link :to="{ name: 'bedroom' }">
                {{ $t("sidebar.bedroom") }}
              </router-link>
            </h3>
          </template>
          <div class="chart-area">
            <img :src="require('@/assets/images/room3.jpg')" />
          </div>
        </card>
      </div>
      <div class="col-md-6" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category"></h5>
            <h3 class="card-title">
              <i class="tim-icons icon-atom text-primary "></i>
              <router-link :to="{ name: 'workroom' }">
                {{ $t("sidebar.workroom") }}
              </router-link>
            </h3>
          </template>
          <div class="chart-area">
            <img :src="require('@/assets/images/workroom.jpg')" />
          </div>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  computed: {
    isRTL() {
      return this.$rtl.isRTL;
    }
  }
};
</script>
<style></style>
