def fair_sharer(values, num_iterations, share=0.1):
    values = list(values)
    n = len(values)

    for _ in range(num_iterations):
        max_index = values.index(max(values))
        rechter_nachbar = (max_index + 1) % n
        linker_nachbar = (max_index - 1) % n
        redistribute = values[max_index] * share

        values[max_index] -= 2 * redistribute
        values[rechter_nachbar] += redistribute
        values[linker_nachbar] += redistribute

    return values

print(fair_sharer([0, 1000, 800, 0], 1))  

