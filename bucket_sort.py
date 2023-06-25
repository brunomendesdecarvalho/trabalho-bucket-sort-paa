import random
import time

# ================================================================================
# BUCKET SORT
# ================================================================================

def bucket_sort(input_list, sub_algorithm_index):
        buckets_list = []

    # Criação dos buckets vazios
        for i in range(len(input_list)):
            buckets_list.append([])

        # Inserção de cada elemento em seu respectivo bucket
        for j in input_list:
            buckets_list[j-1].append(j)

        # Ordenação interna de cada bucket
        for i in range(len(input_list)):
            match sub_algorithm_index:
                case 1:
                    buckets_list[i] = insertion_sort(buckets_list[i])
                case 2:
                    buckets_list[i] = merge_sort(buckets_list[i])
                case 3:
                    buckets_list[i] = quick_sort(buckets_list[i], 0, len(buckets_list[i]) - 1)
                case 4:
                    buckets_list[i] = heap_sort(buckets_list[i])
                case _:
                    buckets_list[i] = insertion_sort(buckets_list[i])

        # Ordenação dos elementos de cada bucket na lista final
        k = 0
        for i in range(len(input_list)):
            for j in range(len(buckets_list[i])):
                input_list[k] = buckets_list[i][j]
                k += 1
        return input_list
    
# ================================================================================
# INSERTION SORT
# ================================================================================

def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var
    return bucket

# ================================================================================
# MERGE SORT
# ================================================================================

def merge_sort(bucket):
    if len(bucket) > 1:

        middle_point = len(bucket)//2

        left_vector = bucket[:middle_point]
        right_vector = bucket[middle_point:]

        merge_sort(left_vector)
        merge_sort(right_vector)

        i = 0
        j = 0
        k = 0

        while i < len(left_vector) and j < len(right_vector):

            if left_vector[i] < right_vector[j]:
                bucket[k]=left_vector[i]
                i += 1
            else:
                bucket[k]=right_vector[j]
                j += 1
            k += 1

        while i < len(left_vector):

            bucket[k]=left_vector[i]
            i += 1
            k += 1

        while j < len(right_vector):
            bucket[k]=right_vector[j]
            j += 1
            k += 1
    return bucket
 
# ================================================================================
# QUICK SORT
# ================================================================================

def partition(array, low, high):
 
    # PIVÔ: ELEMENTO MAIS À DIREITA
    pivot = array[high]
 
    # ÍNDICE DO MAIOR ELEMENTO À ESQUERDA DO PIVÔ
    i = low - 1
 
    # PERCORRER TODOS OS ELEMENTOS E COMPARAR CADA UM COM O PIVÔ
    for j in range(low, high):
        if array[j] <= pivot:
 
            # SE UM ELEMENTO À DIREITA DO PIVÔ É MENOR QUE OUTRO À ESQUERDA, TROCA
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    # TROCA DO PIVÔ PELO ELEMENTO EM I
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # RETORNA POSIÇÃO DO PRÓXIMO PIVÔ
    return i + 1
 
def quick_sort(array, low, high):
    if low < high:
 
        # ENCONTRAR PIVÔ PARA AS SEGUINTES CONDIÇÕES
        # MENORES QUE PIVÔ À ESQUERDA
        # MAIORES QUE PIVÔ À DIREITA
        pi = partition(array, low, high)
 
        # CHAMADA RECURSIVA À ESQUERDA DO PIVÔ
        quick_sort(array, low, pi - 1)
 
        # CHAMADA RECURSIVA À DIREITA DO PIVÔ
        quick_sort(array, pi + 1, high)
    
    return array

# ================================================================================
# HEAP SORT
# ================================================================================

def heapify(array, n, i):
    largest = i  # O MAIOR É A RAIZ DO HEAP
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2
 
 # VÊ SE FOLHA À ESQUERDA EXISTE E SE É MAIOR QUE A RAÍZ
 
    if left < n and array[i] < array[left]:
        largest = left
 
 # VÊ SE FOLHA À DIREITA EXISTE E SE É MAIOR QUE A RAÍZ
 
    if right < n and array[largest] < array[right]:
        largest = right
 
 # MUDA A RAÍZ SE NECESSÁRIO
 
    if largest != i:
        (array[i], array[largest]) = (array[largest], array[i])
 
  # TRANSFORMA A RAÍZ EM HEAP
 
        heapify(array, n, largest)
 
def heap_sort(array):
    n = len(array)
 
 # CRIA UM HEAP MÁXIMO E COMEÇA A PERCORRÊ-LO À PARTIR DA RAÍZ
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
 
 # EXTRAI ELEMENTOS UM POR UM
 
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])  # swap
        heapify(array, i, 0)

    return array


# ================================================================================
# RANDOM LIST GENERATION
# ================================================================================

def generate_n_random_numbers(n):
    i = 0
    y = 0
    vec = []
    while i < n:
        y = random.randint(1,n)
        vec.append(y)
        i += 1
    return vec

# ================================================================================
# MAIN FUNCTION
# ================================================================================
        
def main():
    vector_size = int(input('''
    DIGITE O TAMANHO DA LISTA QUE DESEJA ORDENAR COM O BUCKET SORT:
    >>> '''))
    sub_algorithm_index = input('''
    DIGITE O ÍNDICE DO SUBALGORITMO QUE DESEJA RODAR NO BUCKET SORT:
    1 - INSERTION SORT (PADRÃO)
    2 - MERGE SORT
    3 - QUICK SORT
    4 - HEAP SORT
    OUTROS: INSERTION SORT
    >>> ''')
    input_list = generate_n_random_numbers(vector_size)
    print('LISTA ORIGINAL:')
    print(input_list)
    start_time = time.time()
    if (sub_algorithm_index not in '0123456789'):
        sorted_list = bucket_sort(input_list, 0)
    else:
        sorted_list = bucket_sort(input_list, int(sub_algorithm_index))
    end_time = time.time()
    print('LISTA ORDENADA:')
    print(sorted_list)
    elapsed_time = end_time - start_time
    print('TEMPO TOTAL DE EXECUÇÃO:', elapsed_time, 'SEGUNDOS')

main()