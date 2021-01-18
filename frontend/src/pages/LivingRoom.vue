<template>
  <div>
    <div class="row">
      <div class="col-sm-3" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h4 class="card-title">
              <font-awesome-icon icon="thermometer-full" class="hot" />
              Temperature
            </h4>
          </template>
          <div class="chart-area chart-area-spec">
            <h1 class="text-center">{{ specs.temperature }}<sup>o</sup>C</h1>
          </div>
        </card>
      </div>
      <div class="col-sm-3" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h4 class="card-title">
              <font-awesome-icon icon="tint" class="humidity" /> Humidity
            </h4>
          </template>
          <div class="chart-area chart-area-spec">
            <h1 class="text-center">{{ specs.humidity }}%</h1>
          </div>
        </card>
      </div>
      <div class="col-sm-3" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h4 class="card-title">
              <font-awesome-icon icon="gas-pump" class="gas" /> Gas
            </h4>
          </template>
          <div class="chart-area chart-area-spec">
            <h1 class="text-center">{{ specs.gas }}</h1>
          </div>
        </card>
      </div>
      <div class="col-sm-3" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h4 class="card-title">
              <font-awesome-icon icon="exclamation-triangle" class="status" />
              Status
            </h4>
          </template>
          <div class="chart-area chart-area-spec">
            <h1 class="text-center">{{ specs.status }}</h1>
          </div>
        </card>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <card type="chart">
          <template slot="header">
            <div class="row">
              <div class="col-sm-6" :class="isRTL ? 'text-right' : 'text-left'">
                <h2 class="card-title">Overall</h2>
              </div>
              <div class="col-sm-6">
                <div
                  class="btn-group btn-group-toggle"
                  :class="isRTL ? 'float-left' : 'float-right'"
                  data-toggle="buttons"
                >
                  <label
                    v-for="(option, index) in bigLineChartCategories"
                    :key="option"
                    class="btn btn-sm btn-primary btn-simple"
                    :class="{ active: bigLineChart.activeIndex === index }"
                    :id="index"
                  >
                    <input
                      type="radio"
                      @click="initBigChart(index)"
                      name="options"
                      autocomplete="off"
                      :checked="bigLineChart.activeIndex === index"
                    />
                    {{ option }}
                  </label>
                </div>
              </div>
            </div>
          </template>
          <div class="chart-area">
            <line-chart
              style="height: 100%"
              ref="bigChart"
              chart-id="big-line-chart"
              :chart-data="bigLineChart.chartData"
              :gradient-colors="bigLineChart.gradientColors"
              :gradient-stops="bigLineChart.gradientStops"
              :extra-options="bigLineChart.extraOptions"
            >
            </line-chart>
          </div>
        </card>
      </div>
    </div>
    <div class="row bg-white">
      <div
        class="col-md-12"
        style="margin-top: 60px; margin-bottom: 30px; font-size: 40px; text-align: center; font-weight: bold; color: rgb(5, 4, 100);"
      >
        Device Control Panel
      </div>
      <div class="col-md-6 row">
        <div class="col-md-2"></div>
        <div class="col-md-4">
          <img
            id="door_img"
            :src="require('@/assets/images/door_closed.png')"
            style="margin-top: 25px; width: auto; height: 140px;"
          />
        </div>
        <div class="col-md-6" style="margin-top: 70px;">
          <label class="switch">
            <input type="checkbox" id="door_control" v-model="doorStatus" />
            <span class="slider round"></span>
          </label>
        </div>
      </div>
      <div class="col-md-6 row">
        <div class="col-md-2"></div>
        <div class="col-md-4">
          <img
            id="fan_img"
            :src="require('@/assets/images/fan_off.png')"
            style="margin-top: 25px; width: auto; height: 140px;"
          />
        </div>
        <div class="col-md-6" style="margin-top: 70px;">
          <label class="switch">
            <input type="checkbox" id="fan_control" />
            <span class="slider round"></span>
          </label>
        </div>
      </div>
      <div class="col-md-6 row">
        <div class="col-md-2"></div>
        <div class="col-md-4">
          <img
            id="lamp_img"
            :src="require('@/assets/images/lamp_off.png')"
            style="margin-top: 30px; width: auto; height: 140px;"
          />
        </div>
        <div class="col-md-6" style="margin-top: 80px;">
          <label class="switch">
            <input v-model="lampStatus" type="checkbox" id="lamp_control" />
            <span class="slider round"></span>
          </label>
        </div>
      </div>
      <div class="col-md-6 row">
        <div class="col-md-2"></div>
        <div class="col-md-4">
          <img
            id="tv_img"
            :src="require('@/assets/images/tv_off.png')"
            style="margin-top: 30px; width: auto; height: 140px;"
          />
        </div>
        <div class="col-md-6" style="margin-top: 80px;">
          <label class="switch">
            <input type="checkbox" id="tv_control" />
            <span class="slider round"></span>
          </label>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import LineChart from "@/components/Charts/LineChart";
import BarChart from "@/components/Charts/BarChart";
import * as chartConfigs from "@/components/Charts/config";
import TaskList from "./Dashboard/TaskList";
import UserTable from "./Dashboard/UserTable";
import config from "@/config";
import Vue from "vue";
import VueToast from "vue-toast-notification";
//import "vue-toast-notification/dist/theme-default.css";
import "vue-toast-notification/dist/theme-sugar.css";
Vue.use(VueToast);

import { userService } from "../services";
import { mapState, mapMutations } from "vuex";

export default {
  components: {
    LineChart,
    BarChart,
    TaskList,
    UserTable
  },
  data() {
    return {
      specs: {
        temperature: 20,
        humidity: 50,
        gas: 80,
        status: ""
      },
      bigLineChart: {
        allData: [[], [], []],
        activeIndex: 0,
        chartData: {
          datasets: [{}],
          labels: []
        },
        extraOptions: chartConfigs.purpleChartOptions,
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
        categories: []
      },
      activeIndex: 0,
      lampStatus: false,
      doorStatus: false,
      messagePublish: {
        homeId: 1,
        roomId: 1,
        deviceId: 1,
        value: 1
      }
    };
  },
  created() {
    this.fetchSpec();
  },
  computed: {
    ...mapState("spec", ["time", "temperature", "humidity", "gas"]),
    enableRTL() {
      return this.$route.query.enableRTL;
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
    bigLineChartCategories() {
      return this.$t("dashboard.chartCategories");
    },
    roomStatus() {
      return this.specs.status;
    }
  },
  watch: {
    roomStatus() {
      if (this.roomStatus === "Warning!")
        Vue.$toast.open({
          message: "Gas level is beyond normal. Please check!",
          type: "error",
          duration: 9000
        });
    },
    temperature() {
      this.bigLineChart.allData[0] = this.temperature;
      this.initBigChart(this.activeIndex);
    },
    humidity() {
      this.bigLineChart.allData[2] = this.humidity;
      this.initBigChart(this.activeIndex);
    },
    gas() {
      this.bigLineChart.allData[1] = this.gas;
      this.initBigChart(this.activeIndex);
    },
    lampStatus() {
      let message = "";
      if (this.lampStatus) {
        message = "Turn on the lamp successfully!";
        document
          .getElementById("lamp_img")
          .setAttribute("src", require("@/assets/images/lamp_on.png"));
      } else {
        message = "Turn off the lamp successfully!";
        document
          .getElementById("lamp_img")
          .setAttribute("src", require("@/assets/images/lamp_off.png"));
      }
      this.messagePublish.deviceId = 2;
      this.messagePublish.value = this.lampStatus ? 1 : 0;
      Vue.$toast.open({
        message: message,
        type: "info",
        duration: 3000
      });
      this.publishMessage(this.messagePublish);
    },
    doorStatus() {
      let message = "";
      if (this.doorStatus) {
        message = "Open the door successfully!";
        document
          .getElementById("door_img")
          .setAttribute("src", require("@/assets/images/door_open.png"));
      } else {
        message = "Close the door successfully!";
        document
          .getElementById("door_img")
          .setAttribute("src", require("@/assets/images/door_closed.png"));
      }
      this.messagePublish.deviceId = 1;
      this.messagePublish.value = this.doorStatus ? 1 : 0;
      Vue.$toast.open({
        message: message,
        type: "info",
        duration: 3000
      });
      this.publishMessage(this.messagePublish);
    }
  },
  methods: {
    ...mapMutations("spec", ["addNewSpec"]),
    fetchSpec() {
      userService.getSpecs().then(response => {
        this.specs.temperature = response.temperature;
        this.specs.humidity = response.humidity;
        this.specs.gas = response.gas;
        this.specs.status = response.status;
        this.addNewSpec(response);
      });
      setTimeout(() => {
        this.fetchSpec();
      }, 1000);
    },
    publishMessage(data) {
      userService.publish(data).then(response => {
        console.log(response);
      });
    },
    initBigChart(index) {
      let chartData = {
        datasets: [
          {
            fill: true,
            borderColor: config.colors.primary,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: config.colors.primary,
            pointBorderColor: "rgba(255,255,255,0)",
            pointHoverBackgroundColor: config.colors.primary,
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: this.bigLineChart.allData[index]
          }
        ],
        labels: this.time
      };
      this.$refs.bigChart.updateGradients(chartData);
      this.bigLineChart.chartData = chartData;
      this.bigLineChart.activeIndex = index;
      this.activeIndex = index;
    }
  },
  mounted() {
    this.i18n = this.$i18n;
    if (this.enableRTL) {
      this.i18n.locale = "ar";
      this.$rtl.enableRTL();
    }
    this.initBigChart(0);
  },
  beforeDestroy() {
    if (this.$rtl.isRTL) {
      this.i18n.locale = "en";
      this.$rtl.disableRTL();
    }
  }
};
</script>
<style scoped>
.chart-area-spec {
  height: 60px;
}
.hot {
  color: goldenrod;
}
.humidity {
  color: blue;
}
.status {
  color: red;
}
.gas {
  color: green;
}
.bg-white {
  margin-right: 3px;
  margin-left: 3px;
  padding-bottom: 20px;
}
.switch {
  position: relative;
  display: inline-block;
  width: 80px;
  height: 34px;
}
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}
.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}
input:checked + .slider {
  background-color: #2196f3;
}
input:focus + .slider {
  box-shadow: 0 0 1px #2196f3;
}
input:checked + .slider:before {
  -webkit-transform: translateX(45px);
  -ms-transform: translateX(45px);
  transform: translateX(45px);
}
.slider.round {
  border-radius: 34px;
}
.slider.round:before {
  border-radius: 50%;
}
</style>
