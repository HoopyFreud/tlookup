import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.tlookup',
  appName: 'Tarot',
  webDir: 'dist',
  includePlugins:[
    "@capacitor/android",
    "@capacitor/app",
    "@capacitor/cli",
    "@capacitor/core",
    "@capacitor/haptics",
    "@capacitor/keyboard",
    "@capacitor/status-bar"
  ]
};

export default config;
