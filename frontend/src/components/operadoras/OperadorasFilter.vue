<template>
  <div class="flex flex-wrap gap-2 w-full md:w-auto">
    <button
      @click="emitFilter('top-ano')"
      :class="buttonClasses('top-ano')"
      class="px-4 py-2 rounded-lg transition"
    >
      Top Ano
    </button>
    <button
      @click="emitFilter('top-trimestre')"
      :class="buttonClasses('top-trimestre')"
      class="px-4 py-2 rounded-lg transition"
    >
      Top Trimestre
    </button>
  </div>
</template>

<script setup lang="ts">
import type { PropType } from 'vue';

type FilterRoute = 'top-ano' | 'top-trimestre';

const props = defineProps({
  selectedRoute: {
    type: String as PropType<FilterRoute>,
    required: true
  }
});

const emit = defineEmits<{
  (e: 'filter', value: FilterRoute): void
}>();

const emitFilter = (route: FilterRoute) => {
  emit('filter', route);
};

const buttonClasses = (route: FilterRoute) => ({
  'bg-blue-600 text-white': props.selectedRoute === route,
  'bg-gray-200 hover:bg-gray-300': props.selectedRoute !== route
});
</script>