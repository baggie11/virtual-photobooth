<template>
    <div class="min-h-screen bg-gradient-to-br from-cyan-100 via-pink-50 to-purple-100 relative overflow-hidden font-sans">
      <!-- Confetti Background -->
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
  
      <!-- Floating Emoji Background -->
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
  
      <!-- Gradient Blobs -->
      <div class="absolute top-[-15%] left-[-10%] w-[800px] h-[800px] bg-gradient-to-br from-cyan-300/40 to-pink-300/20 rounded-full blur-[180px] animate-pulse-slow"></div>
      <div class="absolute bottom-[-15%] right-[-10%] w-[800px] h-[800px] bg-gradient-to-tl from-fuchsia-300/40 to-purple-300/20 rounded-full blur-[180px] animate-pulse-slow"></div>
  
      <div class="relative z-10 flex flex-col items-center justify-center text-gray-800 px-6 py-16 sm:py-24">
        <!-- Header -->
        <header :class="['text-center max-w-4xl transition-all duration-1000 ease-out', isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10']">
          <div class="relative inline-block">
            <h1 class="text-5xl sm:text-7xl font-extrabold mb-4 tracking-tight leading-tight bg-clip-text text-transparent bg-gradient-to-r from-fuchsia-500 via-purple-500 to-cyan-400 animate-gradient">
              AI PhotoFiesta!
            </h1>
            <div class="absolute -top-5 -right-5 flex">
              <Star class="w-7 h-7 text-yellow-400 animate-spin" :style="{ animationDuration: '3s' }" />
              <Sparkle class="w-5 h-5 text-cyan-400 animate-ping absolute -bottom-2 -right-2" />
            </div>
          </div>
          <p class="text-xl sm:text-2xl text-gray-700 font-medium mb-6 max-w-2xl mx-auto">Turn your photos into a colorful explosion of fun with AI magic! 🎨✨</p>
          
          <!-- Floating Photo Booth -->
          <div class="relative h-40 mt-10 w-full max-w-3xl mx-auto">
            <div class="absolute inset-0 flex items-center justify-center gap-4">
              <div v-for="(photo, i) in photoStrip" :key="i"
                   class="h-32 w-24 sm:h-40 sm:w-28 rounded-xl shadow-xl overflow-hidden border-4 border-white transition-all duration-500 hover:scale-110 hover:z-10 hover:shadow-2xl"
                   :style="{
                     transform: `rotate(${photo.rotate}deg) translateY(${photo.float}px)`,
                     animation: `float-vertical ${photo.floatSpeed}s ease-in-out infinite alternate`,
                     animationDelay: `${i * 0.2}s`,
                     zIndex: 5 - i,
                     borderColor: photo.borderColor
                   }">
                <div class="w-full h-full bg-gradient-to-br relative" :class="photo.gradient">
                  <span class="absolute top-2 left-2 text-white/80 text-xs font-bold">{{ photo.emoji }}</span>
                </div>
              </div>
            </div>
            <div class="absolute -bottom-6 left-1/2 transform -translate-x-1/2 bg-pink-500 text-white px-4 py-1 rounded-full text-sm font-bold shadow-md">
              Your photos come to life! 🎭
            </div>
          </div>
        </header>
  
    
  
        <!-- CTA Section -->
        <section class="mt-24 w-full max-w-4xl px-6">
          <div class="bg-gradient-to-br from-pink-400 via-purple-500 to-cyan-400 p-8 rounded-3xl border-4 border-white/50 shadow-2xl text-center relative overflow-hidden">
            <div class="absolute -top-20 -right-20 w-40 h-40 rounded-full bg-white/10"></div>
            <div class="absolute -bottom-20 -left-20 w-40 h-40 rounded-full bg-white/10"></div>
            
            <h2 class="text-3xl font-bold mb-4 text-white">Ready for Your Photo Party? 🎉</h2>
            <p class="text-white/90 mb-8 max-w-2xl mx-auto">Join 24,731 happy users creating magical memories!</p>
            
            <router-link
                to="/photo"
                class="inline-block bg-white text-pink-600 font-semibold px-6 py-3 rounded-full shadow-md hover:bg-pink-100 transition-colors duration-300"
                >
                📸 Launch Photo Booth
                </router-link>
             
            
            <div class="flex justify-center mt-8 gap-3 relative z-10">
              <div v-for="(user, i) in sampleUsers" :key="i"
                   class="w-12 h-12 rounded-full border-2 border-white overflow-hidden shadow-lg transform hover:-translate-y-2 transition-transform duration-300"
                   :style="{ transform: `translateX(${-i * 8}px) scale(${1 - i * 0.05})`, zIndex: 5 - i }">
                <div class="w-full h-full flex items-center justify-center text-xl" :class="user.bg">
                  {{ user.emoji }}
                </div>
              </div>
              <div class="w-12 h-12 rounded-full bg-white/90 border-2 border-white flex items-center justify-center text-sm font-bold shadow-lg -ml-3">
                +24K
              </div>
            </div>
          </div>
        </section>
  
        <!-- Footer -->
        <footer class="mt-24 text-center w-full px-6">
          <div class="flex flex-wrap justify-center gap-5 mb-8">
            <a v-for="(item, index) in footerIcons"
               :key="index"
               href="#"
               :class="`group w-14 h-14 rounded-2xl flex items-center justify-center text-2xl bg-white shadow-lg hover:shadow-xl hover:rotate-6 transform hover:scale-110 transition-all duration-300 ${item.hoverBg} ${item.hoverText}`">
              <span class="group-hover:scale-125 transition-transform duration-300">{{ item.icon }}</span>
            </a>
          </div>
          <p class="text-sm text-gray-500 flex flex-wrap items-center justify-center gap-2">
            <span>Made with</span>
            <Heart class="w-5 h-5 text-pink-500 animate-pulse inline" />
            <span>for photo lovers</span>
            <span class="mx-2 hidden sm:inline">•</span>
            <span>© 2024 AI PhotoFiesta</span>
            <span class="mx-2 hidden sm:inline">•</span>
            <a href="#" class="hover:text-cyan-500 transition-colors font-medium">Privacy</a>
            <span class="mx-2">•</span>
            <a href="#" class="hover:text-fuchsia-500 transition-colors font-medium">Terms</a>
            <span class="mx-2">•</span>
            <a href="#" class="hover:text-purple-500 transition-colors font-medium">Careers</a>
          </p>
        </footer>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { Camera, Zap, Music, Heart, Star, Sparkle, ArrowRight, Smile, Share2, Droplet } from 'lucide-vue-next'
  
  const isVisible = ref(false)
  const activeTestimonial = ref(0)
  
  onMounted(() => {
    isVisible.value = true
    setInterval(() => {
      activeTestimonial.value = (activeTestimonial.value + 1) % testimonials.length
    }, 5000)
  })
  
  const photoStrip = [
    { rotate: -3, float: 5, floatSpeed: 3, gradient: 'from-cyan-300 to-blue-400', emoji: '😎', borderColor: 'border-cyan-300' },
    { rotate: 2, float: -8, floatSpeed: 4, gradient: 'from-fuchsia-300 to-purple-400', emoji: '🤩', borderColor: 'border-fuchsia-300' },
    { rotate: -1, float: 10, floatSpeed: 3.5, gradient: 'from-purple-300 to-indigo-400', emoji: '🥳', borderColor: 'border-purple-300' },
    { rotate: 4, float: -5, floatSpeed: 4.5, gradient: 'from-pink-300 to-rose-400', emoji: '🎭', borderColor: 'border-pink-300' },
    { rotate: -2, float: 7, floatSpeed: 3.2, gradient: 'from-blue-300 to-cyan-400', emoji: '✨', borderColor: 'border-blue-300' },
  ]
  
  const features = [
    {
      icon: Camera,
      title: "Smart Capture",
      description: "AI automatically enhances lighting, focus, and composition for perfect shots every time.",
      iconBg: 'bg-cyan-500 shadow-cyan-200',
      bgGradient: 'bg-gradient-to-br from-cyan-200 to-cyan-400',
      borderColor: 'border-cyan-300',
      textColor: 'text-cyan-600',
      emoji: '🤳'
    },
    {
      icon: Zap,
      title: "Pose Genius",
      description: "Real-time AI guidance suggests poses that make you look like a superstar.",
      iconBg: 'bg-fuchsia-500 shadow-fuchsia-200',
      bgGradient: 'bg-gradient-to-br from-fuchsia-200 to-fuchsia-400',
      borderColor: 'border-fuchsia-300',
      textColor: 'text-fuchsia-600',
      emoji: '💃'
    },
    {
      icon: Music,
      title: "Mood Beats",
      description: "AI generates playlists that perfectly match your photo's energy and vibe.",
      iconBg: 'bg-purple-500 shadow-purple-200',
      bgGradient: 'bg-gradient-to-br from-purple-200 to-purple-400',
      borderColor: 'border-purple-300',
      textColor: 'text-purple-600',
      emoji: '🎵'
    },
    {
      icon: Droplet,
      title: "Magic Filters",
      description: "Custom AI filters that adapt to your unique style and preferences.",
      iconBg: 'bg-indigo-500 shadow-indigo-200',
      bgGradient: 'bg-gradient-to-br from-indigo-200 to-indigo-400',
      borderColor: 'border-indigo-300',
      textColor: 'text-indigo-600',
      emoji: '🌈'
    },
    {
      icon: Smile,
      title: "Happy Enhancer",
      description: "AI subtly adjusts expressions to make every smile picture-perfect.",
      iconBg: 'bg-pink-500 shadow-pink-200',
      bgGradient: 'bg-gradient-to-br from-pink-200 to-pink-400',
      borderColor: 'border-pink-300',
      textColor: 'text-pink-600',
      emoji: '😊'
    },
    {
      icon: Share2,
      title: "Instant Sharing",
      description: "One-tap sharing to all platforms with perfect formatting every time.",
      iconBg: 'bg-blue-500 shadow-blue-200',
      bgGradient: 'bg-gradient-to-br from-blue-200 to-blue-400',
      borderColor: 'border-blue-300',
      textColor: 'text-blue-600',
      emoji: '🚀'
    }
  ]
  
  const testimonials = [
    {
      text: "This app turned my boring selfies into art! My Instagram has never looked better.",
      user: { name: "Jamie L.", title: "Influencer", bg: 'bg-gradient-to-br from-amber-200 to-amber-400' },
      textColor: 'text-amber-600'
    },
    {
      text: "The pose suggestions are hilarious and actually work! Family photos are now fun instead of stressful.",
      user: { name: "Marcus T.", title: "Dad of 3", bg: 'bg-gradient-to-br from-rose-200 to-rose-400' },
      textColor: 'text-rose-600'
    },
    {
      text: "I use this for all my product photography now. The AI enhancements save me hours of editing.",
      user: { name: "Sophia K.", title: "Small Business Owner", bg: 'bg-gradient-to-br from-violet-200 to-violet-400' },
      textColor: 'text-violet-600'
    }
  ]
  
  const sampleUsers = [
    { bg: 'bg-gradient-to-br from-amber-200 to-amber-400', emoji: '😍' },
    { bg: 'bg-gradient-to-br from-rose-200 to-rose-400', emoji: '🤗' },
    { bg: 'bg-gradient-to-br from-violet-200 to-violet-400', emoji: '😎' },
    { bg: 'bg-gradient-to-br from-emerald-200 to-emerald-400', emoji: '🥰' },
    { bg: 'bg-gradient-to-br from-sky-200 to-sky-400', emoji: '🤩' }
  ]
  
  const footerIcons = [
    { icon: '📱', hoverBg: 'hover:bg-cyan-100', hoverText: 'hover:text-cyan-600' },
    { icon: '📷', hoverBg: 'hover:bg-fuchsia-100', hoverText: 'hover:text-fuchsia-600' },
    { icon: '💻', hoverBg: 'hover:bg-purple-100', hoverText: 'hover:text-purple-600' },
    { icon: '🎨', hoverBg: 'hover:bg-indigo-100', hoverText: 'hover:text-indigo-600' },
    { icon: '🤳', hoverBg: 'hover:bg-pink-100', hoverText: 'hover:text-pink-600' },
    { icon: '✨', hoverBg: 'hover:bg-yellow-100', hoverText: 'hover:text-yellow-600' },
    { icon: '🎭', hoverBg: 'hover:bg-orange-100', hoverText: 'hover:text-orange-600' },
    { icon: '🌈', hoverBg: 'hover:bg-red-100', hoverText: 'hover:text-red-600' },
  ]
  </script>
  
  <style scoped>
  @keyframes confetti-fall {
    0% {
      transform: translateY(-100vh) rotate(0deg);
    }
    100% {
      transform: translateY(100vh) rotate(360deg);
    }
  }
  
  @keyframes emoji-float {
    0%, 100% {
      transform: translateY(0) translateX(0) rotate(0deg);
    }
    25% {
      transform: translateY(-20px) translateX(10px) rotate(5deg);
    }
    50% {
      transform: translateY(10px) translateX(-10px) rotate(-5deg);
    }
    75% {
      transform: translateY(-10px) translateX(15px) rotate(3deg);
    }
  }
  
  @keyframes float-vertical {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-20px);
    }
  }
  
  @keyframes pulse-slow {
    0%, 100% {
      opacity: 0.3;
      transform: scale(1);
    }
    50% {
      opacity: 0.6;
      transform: scale(1.05);
    }
  }
  
  @keyframes gradient {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }
  
  .animate-pulse-slow {
    animation: pulse-slow 8s ease-in-out infinite;
  }
  
  .animate-gradient {
    background-size: 200% 200%;
    animation: gradient 8s ease infinite;
  }
  </style>