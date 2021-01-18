import DashboardLayout from "@/layout/dashboard/DashboardLayout.vue";

// Admin pages
const Login = () => import("@/pages/Login.vue");
const Home = () => import("@/pages/Home.vue");
const LivingRoom = () => import("@/pages/LivingRoom.vue");
const WorkRoom = () => import("@/pages/WorkRoom.vue");
const BedRoom = () => import("@/pages/BedRoom.vue");
const Kitchen = () => import("@/pages/Kitchen.vue");
const Profile = () => import("@/pages/Profile.vue");

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/home",
    children: [
      {
        path: "home",
        name: "home",
        component: Home
      },
      {
        path: "livingroom",
        name: "livingroom",
        component: LivingRoom
      },
      {
        path: "workroom",
        name: "workroom",
        component: WorkRoom
      },
      {
        path: "bedroom",
        name: "bedroom",
        component: BedRoom
      },
      {
        path: "kitchen",
        name: "kitchen",
        component: Kitchen
      },
      {
        path: "profile",
        name: "profile",
        component: Profile
      }
    ]
  },
  {
    path: "/login",
    component: Login
  },
  { path: "*", redirect: "/" }
];

export default routes;
