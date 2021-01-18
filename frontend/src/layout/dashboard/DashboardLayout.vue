<template>
  <div class="wrapper">
    <side-bar>
      <template slot="links">
        <sidebar-link
          to="/home"
          :name="$t('sidebar.home')"
          icon="tim-icons icon-istanbul"
        />
        <sidebar-link
          to="/livingroom"
          :name="$t('sidebar.livingroom')"
          icon="tim-icons icon-spaceship"
        />
        <sidebar-link
          to="/workroom"
          :name="$t('sidebar.workroom')"
          icon="tim-icons icon-atom"
        />
        <sidebar-link
          to="/bedroom"
          :name="$t('sidebar.bedroom')"
          icon="tim-icons icon-app"
        />
        <sidebar-link
          to="/kitchen"
          :name="$t('sidebar.kitchen')"
          icon="tim-icons icon-shape-star"
        />
        <sidebar-link
          to="/profile"
          :name="$t('sidebar.userProfile')"
          icon="tim-icons icon-single-02"
        />
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click.native="toggleSidebar"> </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
export default {
  components: {
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  }
};
</script>
