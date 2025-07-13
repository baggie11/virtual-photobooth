<!-- components/StyleSelector.vue -->
<template>
  <div class="bg-white/70 backdrop-blur-sm rounded-2xl p-6 shadow-xl border border-white">
    <h2 class="text-2xl font-bold text-center text-transparent bg-clip-text bg-gradient-to-r from-fuchsia-500 via-purple-500 to-cyan-500 mb-6">
      🎨 Choose a Style
    </h2>
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-6">
      <div 
        v-for="style in styles" 
        :key="style.name"
        class="rounded-xl overflow-hidden shadow-md transform hover:scale-105 transition cursor-pointer border-4"
        :class="selected === style.name ? 'border-purple-500' : 'border-transparent'"
        @click="selectStyle(style.name)"
      >
        <img :src="style.preview" alt="style preview" class="w-full h-40 object-cover" :class="style.class" />
        <div class="p-2 text-center font-semibold text-gray-700">{{ style.label }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'

const emit = defineEmits(['update:style'])

const selected = ref('none')

const styles = [
  { name: 'none', label: 'Original', preview: '/styles/original.jpg', class: '' },
  { name: 'grayscale', label: 'Grayscale', preview: '/styles/original.jpg', class: 'grayscale' },
  { name: 'sepia', label: 'Sepia', preview: '/styles/original.jpg', class: 'sepia' },
  { name: 'contrast', label: 'High Contrast', preview: '/styles/original.jpg', class: 'contrast-200' },
  { name: 'invert', label: 'Invert', preview: '/styles/original.jpg', class: 'invert' },
  { name: 'blur', label: 'Blur', preview: '/styles/original.jpg', class: 'blur-sm' }
]

const selectStyle = (styleName) => {
  selected.value = styleName
  emit('update:style', styleName)
}
</script>

<style scoped>
.grayscale {
  filter: grayscale(100%);
}
.sepia {
  filter: sepia(100%);
}
.invert {
  filter: invert(100%);
}
.blur-sm {
  filter: blur(2px);
}
</style>
