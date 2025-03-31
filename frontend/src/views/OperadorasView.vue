<template>
  <div class="flex flex-col gap-4 max-w-[1500px] mx-auto my-18">
    <div class="flex justify-between"> 
      <OperadorasSearch 
        v-model="searchQuery"
        @search="onSearch"
      />
    
    <OperadorasFilter
      :selected-route="selectedRoute"
      @filter="(route) => {
        searchQuery = '';
        fetchData(route);
    }"
  />
    </div>
    
    <OperadorasTable
      :headers="tableHeaders"
      :data="sortedData"
      :loading="loading"
      :search-query="searchQuery"
      @sort="sortTable"
    />
    
    <OperadorasPagination
      v-if="!loading && data.length > 0"
      :current-page="currentPage"
      :items-per-page="itemsPerPage"
      :total-items="data.length"
      @prev="currentPage--"
      @next="currentPage++"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import OperadorasSearch from '@/components/operadoras/OperadorasSearch.vue'
import OperadorasFilter from '@/components/operadoras/OperadorasFilter.vue'
import OperadorasTable from '@/components/operadoras/OperadorasTable.vue'
import OperadorasPagination from '@/components/operadoras/OperadorasPagination.vue'
import { useOperadoras } from '@/composables/useOperadoras.ts'

const {
  data,
  loading,
  searchQuery,
  selectedRoute,
  tableHeaders,
  sortedData,
  currentPage,
  itemsPerPage,
  fetchData,
  onSearch,
  sortTable
} = useOperadoras()

onMounted(() => {
  fetchData('top-ano')
})
</script>