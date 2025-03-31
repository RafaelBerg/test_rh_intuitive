import { ref, computed } from 'vue';
import api from '../lib/axios';

interface Operadora {
  razao_social: string;
  nome_fantasia?: string;
  modalidade?: string;
  telefone?: string;
  email?: string;
  cidade?: string;
  uf?: string;
  despesas_totais?: number;
  ddd?: string;
}

interface TableHeader {
  key: string;
  label: string;
}

export function useOperadoras() {
  const data = ref<Operadora[]>([]);
  const loading = ref(false);
  const searchQuery = ref('');
  const selectedRoute = ref<'top-ano' | 'top-trimestre' | null>('top-ano');
  const sortKey = ref<string>('razao_social');
  const sortDirection = ref(1);
  const currentPage = ref(1);
  const itemsPerPage = 10;
  const isSearchActive = ref(false);

  const tableHeaders = computed<TableHeader[]>(() => {
    if (isSearchActive.value) {
      return [
        { key: 'razao_social', label: 'Razão Social' },
        { key: 'nome_fantasia', label: 'Nome Fantasia' },
        { key: 'modalidade', label: 'Modalidade' },
        { key: 'telefone', label: 'Telefone' },
        { key: 'email', label: 'E-mail' },
        { key: 'cidade', label: 'Cidade' },
        { key: 'uf', label: 'UF' }
      ];
    } else {
      return [
        { key: 'razao_social', label: 'Razão Social' },
        { key: 'despesas_totais', label: 'Despesas Totais' }
      ];
    }
  });

  const sortedData = computed<Operadora[]>(() => {
    const sorted = [...data.value].sort((a, b) => {
      const aValue = a[sortKey.value as keyof Operadora];
      const bValue = b[sortKey.value as keyof Operadora];
      
      const safeAValue = aValue === undefined 
        ? (sortKey.value === 'despesas_totais' ? 0 : '')
        : aValue;
      
      const safeBValue = bValue === undefined 
        ? (sortKey.value === 'despesas_totais' ? 0 : '')
        : bValue;
  
      if (sortKey.value === 'despesas_totais') {
        return (Number(safeAValue) - Number(safeBValue)) * sortDirection.value;
      }
      
      return String(safeAValue).localeCompare(String(safeBValue)) * sortDirection.value;
    });
  
    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return sorted.slice(start, end);
  });

  const formatCurrency = (value?: number): string => {
    if (!value) return 'R$ 0,00';
    return `R$ ${value.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, '.')}`;
  };

  const sortTable = (key: string): void => {
    if (sortKey.value === key) {
      sortDirection.value *= -1;
    } else {
      sortKey.value = key;
      sortDirection.value = 1;
    }
  };

  const fetchData = async (route: 'top-ano' | 'top-trimestre'): Promise<void> => {
    loading.value = true;
    selectedRoute.value = route;
    currentPage.value = 1;
    isSearchActive.value = false;
    searchQuery.value = '';
    
    try {
      const endpoint = route === 'top-ano' ? '/operadoras/top-ano' : '/operadoras/top-trimestre';
      const response = await api.get<Operadora[]>(endpoint);
      data.value = response.data;
    } catch (error) {
      console.error('Error fetching data:', error);
      data.value = [];
    } finally {
      loading.value = false;
    }
  };

  const onSearch = async (): Promise<void> => {
    if (!searchQuery.value.trim()) return;
    
    loading.value = true;
    selectedRoute.value = null;
    currentPage.value = 1;
    isSearchActive.value = true;
    
    try {
      const response = await api.get<{ operadoras?: Operadora[] } | Operadora[]>(
        '/operadoras',
        { params: { search: searchQuery.value } }
      );
      
      if (response.data && 'operadoras' in response.data) {
        data.value = response.data.operadoras || [];
      } else {
        data.value = Array.isArray(response.data) ? response.data : [];
      }
    } catch (error) {
      console.error('Error searching:', error);
      data.value = [];
    } finally {
      loading.value = false;
    }
  };

  return {
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
    formatCurrency,
    sortTable,
    sortKey
  };
}