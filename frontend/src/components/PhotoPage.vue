<template>
    <div class="min-h-screen bg-gradient-to-br from-cyan-100 via-pink-50 to-purple-100 py-12 px-4 sm:px-6 font-sans">
        <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div v-for="i in 60" :key="i" 
             class="absolute rounded-sm opacity-70"
             :class="['bg-cyan-400', 'bg-fuchsia-400', 'bg-purple-400', 'bg-yellow-300', 'bg-pink-400'][Math.floor(Math.random() * 5)]"
             :style="{
               width: `${Math.random() * 12 + 4}px`,
               height: `${Math.random() * 8 + 4}px`,
               top: `${Math.random() * 100}%`,
               left: `${Math.random() * 100}%`,
               transform: `rotate(${Math.random() * 360}deg)`,
               animation: `confetti-fall ${Math.random() * 10 + 5}s linear infinite`,
               animationDelay: `${Math.random() * 5}s`
             }"></div>
      </div>
        <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div v-for="i in 15" :key="i" 
             class="absolute text-2xl opacity-20"
             :style="{
               top: `${Math.random() * 100}%`,
               left: `${Math.random() * 100}%`,
               animation: `emoji-float ${Math.random() * 20 + 10}s linear infinite`,
               animationDelay: `${Math.random() * 10}s`
             }">
          {{ ['🌈', '🎨', '📸', '✨', '🎉', '🤩', '👯', '💃', '🕺', '🎊'][Math.floor(Math.random() * 10)] }}
        </div>
      </div>
      <div class="max-w-6xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-12">
          <div class="inline-block bg-white/30 backdrop-blur-sm rounded-2xl px-6 py-3 shadow-sm mb-6">
            <h1 class="text-4xl sm:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-fuchsia-500 via-purple-500 to-cyan-500 mb-2">
              🎥 Create Your Photo Strip
            </h1>
          </div>
          <p class="text-lg text-gray-700 max-w-2xl mx-auto">Capture moments or upload photos to create a personalized photo strip with fun effects! 📸</p>
        </div>
  
        <!-- Main Content -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
          <!-- Left Column - Pose Recommendations & Style Selection -->
          <div class="lg:col-span-3 bg-white/70 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-white">
            <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-pink-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
              Pose Ideas
            </h2>
            <!-- Pinterest Button -->
            <div class="border-t border-gray-200 pt-4">
                <button 
                @click="openPinterestPopup"
                class="w-full flex items-center justify-center gap-2 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white px-4 py-3 rounded-full shadow-md transition-all"
                >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12.17 1.27a.73.73 0 00-.53-.25.74.74 0 00-.53.25l-5 5.19A5 5 0 004.25 12a5.19 5.19 0 001.57 3.78 5.47 5.47 0 003.8 1.57 4.91 4.91 0 002.39-.66 1.61 1.61 0 01.76-.2 1.18 1.18 0 011.18 1.18 1.52 1.52 0 01-.4 1 5.28 5.28 0 01-3.93 1.66 7.79 7.79 0 01-5.32-2L2.29 21.4a.75.75 0 000 1.06.77.77 0 001.07 0l2.81-2.81a8.15 8.15 0 005 2 8.23 8.23 0 005.9-2.36 8.36 8.36 0 002.36-5.9 8.22 8.22 0 00-2.36-5.9zm-.6 10.72a3.76 3.76 0 01-3.75-3.75 3.64 3.64 0 011-2.64l3.53-3.66 3.57 3.71a3.69 3.69 0 011 2.65 3.76 3.76 0 01-3.75 3.75z"/>
                </svg>
                Group Pose Ideas
                </button>
                
                <button 
                @click="openPinterestPopupSingle"
                class="w-full flex items-center mt-[20px] justify-center gap-2 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white px-4 py-3 rounded-full shadow-md transition-all"
                >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12.17 1.27a.73.73 0 00-.53-.25.74.74 0 00-.53.25l-5 5.19A5 5 0 004.25 12a5.19 5.19 0 001.57 3.78 5.47 5.47 0 003.8 1.57 4.91 4.91 0 002.39-.66 1.61 1.61 0 01.76-.2 1.18 1.18 0 011.18 1.18 1.52 1.52 0 01-.4 1 5.28 5.28 0 01-3.93 1.66 7.79 7.79 0 01-5.32-2L2.29 21.4a.75.75 0 000 1.06.77.77 0 001.07 0l2.81-2.81a8.15 8.15 0 005 2 8.23 8.23 0 005.9-2.36 8.36 8.36 0 002.36-5.9 8.22 8.22 0 00-2.36-5.9zm-.6 10.72a3.76 3.76 0 01-3.75-3.75 3.64 3.64 0 011-2.64l3.53-3.66 3.57 3.71a3.69 3.69 0 011 2.65 3.76 3.76 0 01-3.75 3.75z"/>
                </svg>
                Single Pose Ideas
                </button>

              <p class="text-xs text-gray-500 mt-2 text-center">Get more pose ideas from Pinterest</p>
            </div>

            <!-- Style Selection -->
            <div class="mt-8 border-t border-gray-200 pt-6">
              <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-cyan-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01" />
                </svg>
                Select Style
              </h2>
              
              <div class="grid grid-cols-2 gap-3">
                <button 
                  v-for="style in styles" 
                  :key="style.id"
                  @click="selectStyle(style)"
                  class="relative overflow-hidden rounded-lg aspect-square group"
                  :class="{ 'ring-2 ring-offset-2 ring-purple-500': selectedStyle?.id === style.id }"
                >
                  <img 
                    :src="style.thumbnail" 
                    :alt="style.name" 
                    class="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
                  >
                  <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end p-2">
                    <span class="text-white font-medium text-sm">{{ style.name }}</span>
                  </div>
                </button>
              </div>
              
              <button 
                @click="applyStyleToPhotos" 
                :disabled="!selectedStyle || photoStrip.length === 0 || isProcessing"
                class="w-full mt-4 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white px-4 py-3 rounded-full shadow-md transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 animate-spin" fill="none" viewBox="0 0 24 24" stroke="currentColor" v-if="isProcessing">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                {{ isProcessing ? 'Processing...' : 'Apply Style' }}
              </button>
            </div>
          </div>
  
          <!-- Middle Column - Camera & Upload -->
          <div class="lg:col-span-6 space-y-8">
            <!-- Webcam Preview -->
            <div class="relative group bg-white/70 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-white">
              <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-purple-500" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M4 5a2 2 0 00-2 2v8a2 2 0 002 2h12a2 2 0 002-2V7a2 2 0 00-2-2h-1.586a1 1 0 01-.707-.293l-1.121-1.121A2 2 0 0011.172 3H8.828a2 2 0 00-1.414.586L6.293 4.707A1 1 0 015.586 5H4zm6 9a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd" />
                </svg>
                Camera
              </h2>
              <div class="relative aspect-[4/3] bg-gradient-to-br from-purple-100 to-cyan-100 rounded-xl overflow-hidden shadow-lg">
                <video ref="videoRef" autoplay playsinline class="w-full h-full object-cover"></video>
                <!-- Centered capture button at bottom -->
                <div class="absolute bottom-4 left-0 right-0 flex items-center justify-center">
                  <button @click="capturePhoto" class="bg-white/90 hover:bg-white transition-all duration-300 p-4 rounded-full shadow-xl border-2 border-purple-200 hover:border-purple-300 group-hover:scale-110">
                    <div class="bg-gradient-to-r from-pink-500 to-purple-500 rounded-full p-3 group-hover:from-pink-600 group-hover:to-purple-600 transition-all">
                      <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-white" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M4 5a2 2 0 00-2 2v8a2 2 0 002 2h12a2 2 0 002-2V7a2 2 0 00-2-2h-1.586a1 1 0 01-.707-.293l-1.121-1.121A2 2 0 0011.172 3H8.828a2 2 0 00-1.414.586L6.293 4.707A1 1 0 015.586 5H4zm6 9a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd" />
                      </svg>
                    </div>
                  </button>
                </div>
              </div>
            </div>
  
            <!-- Upload Section -->
            <div class="bg-white/70 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-white">
              <h2 class="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-fuchsia-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
                Upload Photos
              </h2>
              <div class="border-2 border-dashed border-gray-300 rounded-xl p-8 text-center cursor-pointer hover:border-purple-400 transition-colors bg-gradient-to-br from-gray-50 to-gray-100"
                   @click="handleUploadClick">
                <input type="file" ref="fileInput" @change="handleUpload" accept="image/*" multiple class="hidden">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mx-auto text-gray-400 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                <p class="text-gray-700 mb-2">Drag & drop photos here or click to browse</p>
                <p class="text-sm text-gray-500">Supports JPG, PNG (max 5MB each)</p>
              </div>
            </div>
          </div>
  
          <!-- Right Column - Photo Strip -->
          <div class="lg:col-span-3 bg-white/70 backdrop-blur-sm rounded-2xl p-6 shadow-lg border border-white">
            <div class="flex justify-between items-center mb-4">
              <h2 class="text-xl font-bold text-gray-800 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-fuchsia-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                </svg>
                Your Photo Strip
              </h2>
              <button 
                @click="clearPhotos" 
                class="text-sm text-red-500 hover:text-red-600 transition-colors flex items-center gap-1"
                v-if="photoStrip.length > 0"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                Clear All
              </button>
            </div>
  
            <!-- Empty State -->
            <div v-if="photoStrip.length === 0" class="flex flex-col items-center justify-center h-full py-12 text-center">
              <div class="bg-gradient-to-r from-cyan-100 to-pink-100 p-4 rounded-full mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-purple-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 class="text-lg font-bold text-gray-800 mb-2">Your photo strip is empty</h3>
              <p class="text-gray-600 mb-6">Capture or upload photos to get started!</p>
            </div>
  
            <!-- Photo Strip -->
            <div v-else class="space-y-4">
              <div class="relative w-full overflow-y-auto flex flex-col gap-4 items-center py-4 px-2 h-[500px]">
                <div 
                  v-for="(photo, index) in photoStrip" 
                  :key="index"
                  class="flex-shrink-0 h-40 w-56 rounded-lg overflow-hidden shadow-lg relative group transition-all duration-300 hover:shadow-xl"
                  :style="{ transform: `rotate(${photo.rotate}deg)`, borderColor: photo.borderColor }"
                >
                  <img :src="photo.src" alt="photo" class="w-full h-full object-cover" />
                  <button 
                    @click="removePhoto(index)" 
                    class="absolute top-2 right-2 bg-red-500 text-white rounded-full p-1 opacity-0 group-hover:opacity-100 transition-opacity duration-200 shadow-md"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div>
              </div>
              
              <button 
                @click="downloadStrip" 
                class="w-full bg-gradient-to-r from-fuchsia-500 to-purple-600 hover:from-fuchsia-600 hover:to-purple-700 text-white px-6 py-3 rounded-full shadow-lg flex items-center justify-center gap-2 transition-all duration-300 hover:scale-[1.02] mt-4"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
                Download Photo Strip
              </button>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Pinterest Modal -->
      <div v-if="showPinterestModal" class="fixed inset-0 z-50 overflow-y-auto">
        <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <!-- Background overlay -->
          <div class="fixed inset-0 transition-opacity" aria-hidden="true">
            <div class="absolute inset-0 bg-gray-500 bg-opacity-75" @click="showPinterestModal = false"></div>
          </div>
  
          <!-- Modal container -->
          <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-4xl sm:w-full">
            <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div class="sm:flex sm:items-start">
                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
                  <div class="flex justify-between items-center mb-4">
                    <h3 class="text-lg leading-6 font-medium text-gray-900">
                      Pinterest Pose Inspiration
                    </h3>
                    <button @click="showPinterestModal = false" class="text-gray-400 hover:text-gray-500">
                      <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                      </svg>
                    </button>
                  </div>
                  <div class="mt-2">
                    <iframe 
                      src="https://pin.it/15NAt5tKm" 
                      height="600" 
                      width="100%" 
                      frameborder="0" 
                      scrolling="yes" 
                      class="rounded-lg"
                    ></iframe>
                  </div>
                </div>
              </div>
            </div>
            <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
              <button 
                type="button" 
                class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
                @click="showPinterestModal = false"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const videoRef = ref(null)
const stream = ref(null)
const photoStrip = ref([])
const fileInput = ref(null)
const showPinterestModal = ref(false)
const selectedStyle = ref(null)
const isProcessing = ref(false)

const styles = ref([
  {
    id: 'vintage',
    name: 'Vintage',
    thumbnail: 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
    description: 'Classic film camera look with faded colors'
  },
  {
    id: 'blackwhite',
    name: 'Black & White',
    thumbnail: 'https://images.unsplash.com/photo-1519125323398-675f0ddb6308?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
    description: 'Timeless monochrome style'
  },
  {
    id: 'polaroid',
    name: 'Polaroid',
    thumbnail: 'https://images.unsplash.com/photo-1528720208104-3d9bd03cc9d4?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
    description: 'Instant film aesthetic with white border'
  },
  {
    id: 'dreamy',
    name: 'Dreamy',
    thumbnail: 'https://images.unsplash.com/photo-1511499767150-a48a237f0083?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
    description: 'Soft focus and glowing highlights'
  }
])

const startCamera = async () => {
  try {
    stream.value = await navigator.mediaDevices.getUserMedia({
      video: {
        width: { ideal: 1280 },
        height: { ideal: 720 },
        facingMode: 'user'
      }
    })
    videoRef.value.srcObject = stream.value
  } catch (error) {
    console.error('Camera error:', error)
    alert('Could not access the camera. Please check permissions.')
  }
}

const capturePhoto = () => {
  const video = videoRef.value;
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Convert canvas to Blob
  canvas.toBlob((blob) => {
    const file = new File([blob], `photo-${Date.now()}.jpg`, { type: 'image/jpeg' });
    const imageUrl = URL.createObjectURL(blob);
    addToPhotoStrip(imageUrl, file);
  }, 'image/jpeg', 0.9);
};

const applyStyleToPhotos = async () => {
  if (!selectedStyle.value || photoStrip.value.length === 0) return;

  isProcessing.value = true;

  try {
    const styledPhotos = [];

    for (const photo of photoStrip.value) {
      if (!photo.file) {
        console.warn("No file found in photo object. Skipping...");
        continue;
      }

      const formData = new FormData();
      formData.append("image", photo.file);
      formData.append("style", selectedStyle.value.id); // e.g., "Picasso_Selfportrait_5000"

      const response = await fetch("http://127.0.0.1:5000/style-transfer", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Style transfer failed (HTTP ${response.status})`);
      }

      console.log(response);

      const styledBlob = await response.blob();
      const styledUrl = URL.createObjectURL(styledBlob);

      styledPhotos.push({
        src: styledUrl, // for <img :src="photo.src" />
        file: new File([styledBlob], `styled-${Date.now()}.jpg`, {
          type: 'image/jpeg'
        }),
        rotate: photo.rotate || 0,
        borderColor: photo.borderColor || '#000',
      });
    }

    photoStrip.value = styledPhotos;
  } catch (error) {
    console.error("Error applying style:", error);
    alert(`Failed to apply style: ${error.message}`);
  } finally {
    isProcessing.value = false;
  }
};

const handleUploadClick = () => {
  fileInput.value.click()
}

const handleUpload = (event) => {
  const files = event.target.files
  if (!files.length) return

  Array.from(files).forEach(file => {
    if (!file.type.match('image.*')) {
      alert('Please upload only image files')
      return
    }

    const reader = new FileReader()
    reader.onload = (e) => {
      addToPhotoStrip(e.target.result, file)
    }
    reader.readAsDataURL(file)
  })
}

const addToPhotoStrip = (src, file) => {
  photoStrip.value.unshift({
    src,
    file,
    rotate: Math.floor(Math.random() * 8 - 4),
    borderColor: getRandomColor()
  })
}

const getRandomColor = () => {
  const colors = ['#7dd3fc', '#a5b4fc', '#d8b4fe', '#f9a8d4', '#67e8f9']
  return colors[Math.floor(Math.random() * colors.length)]
}

const removePhoto = (index) => {
  photoStrip.value.splice(index, 1)
}

const clearPhotos = () => {
  photoStrip.value = []
}

const downloadStrip = () => {
  if (!photoStrip.value.length) return

  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')
  const width = 1300
  const height = 1000
  const padding = 50
  const borderWidth = 4

  canvas.width = width + padding * 2
  canvas.height = (height + padding) * Math.min(photoStrip.value.length, 4) + padding

  ctx.fillStyle = '#fdf4ff'
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  let loaded = 0
  const images = photoStrip.value.slice(0, 4)

  images.forEach((photo, index) => {
    const x = padding
    const y = padding + index * (height + padding)
    const img = new Image()
    img.onload = () => {
      ctx.save()
      ctx.translate(x + width / 2, y + height / 2)
      ctx.rotate(photo.rotate * Math.PI / 180)
      ctx.drawImage(img, -width / 2, -height / 2, width, height)
      ctx.restore()

      loaded++
      if (loaded === images.length) {
        const link = document.createElement('a')
        link.download = 'photo-strip.png'
        link.href = canvas.toDataURL('image/png')
        link.click()
      }
    }
    img.src = photo.src
  })
}

const openPinterestPopup = () => {
  showPinterestModal.value = true
}

const openPinterestPopupSingle = () => {
  showPinterestModal.value = true
}

const selectStyle = (style) => {
  selectedStyle.value = style
}

onMounted(() => {
  startCamera()
})

onBeforeUnmount(() => {
  if (stream.value) {
    stream.value.getTracks().forEach(track => track.stop())
  }
})
</script>

<style>
@keyframes confetti-fall {
  0% {
    transform: translateY(-100vh) rotate(0deg);
  }
  100% {
    transform: translateY(100vh) rotate(360deg);
  }
}

@keyframes emoji-float {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 0.2;
  }
  50% {
    opacity: 0.5;
  }
  100% {
    transform: translateY(-100vh) rotate(360deg);
    opacity: 0;
  }
}
</style>