#include <random>
#include <thread>

namespace Engine {
    thread_local static std::random_device hardware_seed;
    thread_local static std::mt19937 random_engine{hardware_seed()};
}

template<typename Integer>
auto generate_integer(Integer low_limit, Integer high_limit) -> Integer {
    std::uniform_int_distribution<Integer> distribution{low_limit, high_limit};
    return distribution(Engine::random_engine);
}

template<typename Float>
auto generate_float(Float low_limit, Float high_limit) -> Float {
    std::uniform_real_distribution<Float> distribution{low_limit, high_limit};
    return distribution(Engine::random_engine);
}
