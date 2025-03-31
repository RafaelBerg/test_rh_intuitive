<template>
  <div class="flex flex-col md:flex-row gap-4 w-full md:w-auto">
    <div class="relative flex-grow">
      <input
        :value="modelValue"
        @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
        type="text"
        placeholder="Pesquisar Operadora..."
        class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        @keyup.enter="$emit('search')"
      />
      <button
        @click="$emit('search')"
        class="absolute right-2 top-1/2 transform -translate-y-1/2 bg-blue-500 text-white p-1 rounded-md hover:bg-blue-600 transition"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';

defineProps<{ modelValue: string }>();

defineEmits<{ 
  (event: 'update:modelValue', value: string): void;
  (event: 'search'): void;
}>();
</script>