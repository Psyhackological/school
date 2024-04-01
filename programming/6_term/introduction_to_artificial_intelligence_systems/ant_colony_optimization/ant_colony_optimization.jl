import Pkg
Pkg.add("Distributions")
Pkg.add("StatsBase")
using Random, Distributions, StatsBase

function distance(city1::Tuple{Int, Int}, city2::Tuple{Int, Int})::Float64
    sqrt((city1[1] - city2[1])^2 + (city1[2] - city2[2])^2)
end

function city_select(pheromone::Dict{String, Dict{String, Float64}}, current_city::String, unvisited_cities::Dict{String, Tuple{Int, Int}}, alpha::Float64, beta::Float64, cities::Dict{String, Tuple{Int, Int}})
    probabilities = Array{Float64}(undef, length(unvisited_cities))
    city_indices = collect(keys(unvisited_cities))
    for (index, city) in enumerate(city_indices)
        city_distance = distance(cities[current_city], unvisited_cities[city])
        probabilities[index] = (pheromone[current_city][city] ^ alpha) * ((1.0 / city_distance) ^ beta)
    end
    chosen_city = city_indices[sample(1:length(city_indices), Weights(probabilities))]
    delete!(unvisited_cities, chosen_city)
    return chosen_city, unvisited_cities
end

function pheromone_update(pheromone::Dict{String, Dict{String, Float64}}, cities::Dict{String, Tuple{Int, Int}}, pheromone_evaporation::Float64, ants_route::Vector{Vector{String}}, q::Float64, best_path::Vector{String}, best_distance::Float64)
    for city1 in keys(cities), city2 in keys(cities)
        pheromone[city1][city2] *= pheromone_evaporation
    end
    for route in ants_route
        total_distance = sum(distance(cities[route[i]], cities[route[i + 1]]) for i in 1:length(route) - 1)
        delta_pheromone = q / total_distance
        for i in 1:length(route) - 1
            pheromone[route[i]][route[i + 1]] += delta_pheromone
            pheromone[route[i + 1]][route[i]] += delta_pheromone
        end
        if total_distance < best_distance
            best_path = route
            best_distance = total_distance
        end
    end
    return pheromone, best_path, best_distance
end

function main(cities::Dict{String, Tuple{Int, Int}}, start_city::String, ants_num::Int, iterations_num::Int, pheromone_evaporation::Float64, alpha::Float64, beta::Float64, q::Float64)
    pheromone = Dict(city => Dict(other_city => 1.0 for other_city in keys(cities)) for city in keys(cities))
    best_path = String[]
    best_distance = Inf
    for _ in 1:iterations_num
        ants_route = Vector{Vector{String}}()
        for _ in 1:ants_num
            unvisited_cities = deepcopy(cities)
            current_city = haskey(cities, start_city) ? start_city : rand(keys(unvisited_cities))
            delete!(unvisited_cities, current_city)
            ant_route = [current_city]
            while !isempty(unvisited_cities)
                current_city, unvisited_cities = city_select(pheromone, current_city, unvisited_cities, alpha, beta, cities)
                push!(ant_route, current_city)
            end
            push!(ant_route, ant_route[1])
            push!(ants_route, ant_route)
        end
        pheromone, best_path, best_distance = pheromone_update(pheromone, cities, pheromone_evaporation, ants_route, q, best_path, best_distance)
    end
    return best_path, best_distance
end

# Entry point
begin
    cities = Dict("A" => (0, 0), "D" => (1, 8), "F" => (2, 10), "G" => (3, 3), "B" => (4, 7), "E" => (6, 4), "C" => (8, 13))
    START_CITY = "A"
    best_path, best_distance = main(cities, START_CITY, length(cities) * 2, 1200, 0.7, 1.0, 5.0, 10.0)
    println("$best_distance distance for $(join(best_path, " -> "))")
end
