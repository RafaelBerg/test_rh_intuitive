<template>
  <div class="overflow-x-auto bg-white rounded-lg shadow">
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th 
            v-for="(header, index) in headers" 
            :key="index"
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
            @click="$emit('sort', header.key)"
          >
            <div class="flex items-center">
              {{ header.label }}
              <span v-if="sortKey === header.key" class="ml-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z" clip-rule="evenodd" />
                </svg>
              </span>
            </div>
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <OperadorasLoader v-if="loading" :columns="headers.length" />
        
        <template v-else>
          <tr v-if="data.length > 0" v-for="(item, index) in data" :key="index" class="hover:bg-gray-50 even:bg-gray-100">
            <td v-for="(header, hIndex) in headers" :key="hIndex" class="px-6 py-4 whitespace-nowrap">
              <div v-if="header.key === 'despesas_totais'" class="text-sm font-medium text-gray-900">
                {{ formatCurrency(item[header.key]) }}
              </div>
              <div v-else-if="header.key === 'telefone'" class="text-sm text-gray-500">
                ({{ item.ddd }}) {{ item[header.key] }}
              </div>
              <div v-else class="text-sm text-gray-900">
                {{ item[header.key] || 'N/A' }}
              </div>
            </td>
          </tr>
          
          <tr v-else>
            <td :colspan="headers.length" class="px-6 py-4 text-center text-sm text-gray-500">
              Nenhum resultado encontrado para "{{ searchQuery }}"
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import OperadorasLoader from './OperadorasLoader.vue';

interface Header {
  key: string;
  label: string;
}

interface DataItem {
  [key: string]: any;
  ddd?: string;
}

defineProps<{
  headers: Header[];
  data: DataItem[];
  loading?: boolean;
  searchQuery?: string;
  sortKey?: string;
}>();

defineEmits<{
  (event: 'sort', key: string): void;
}>();

const formatCurrency = (value?: number): string => {
  if (!value) return 'R$ 0,00';
  return `R$ ${value.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, '.')}`;
};
</script>