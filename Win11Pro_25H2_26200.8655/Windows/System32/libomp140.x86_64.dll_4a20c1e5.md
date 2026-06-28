# Binary Specification: libomp140.x86_64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\libomp140.x86_64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a20c1e5c115c29771a12324513eb109badac72180f79481527ad79d996ffb33`
* **Total Exported Functions:** 786

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 162 | `__kmpc_aligned_alloc` | `0x35C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `__kmpc_alloc` | `0x35D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `__kmpc_calloc` | `0x35E0` | 160 | UnwindData |  |
| 165 | `__kmpc_destroy_allocator` | `0x3680` | 70 | UnwindData |  |
| 167 | `__kmpc_free` | `0x36D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `__kmpc_get_default_allocator` | `0x36E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `__kmpc_init_allocator` | `0x3700` | 7 | UnwindData |  |
| 174 | `__kmpc_realloc` | `0x3A50` | 152 | UnwindData |  |
| 185 | `__kmpc_set_default_allocator` | `0x3AF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `kmpc_aligned_malloc` | `0x3B20` | 117 | UnwindData |  |
| 200 | `kmpc_calloc` | `0x3BA0` | 112 | UnwindData |  |
| 201 | `kmpc_free` | `0x3C10` | 24 | UnwindData |  |
| 206 | `kmpc_malloc` | `0x3C80` | 55 | UnwindData |  |
| 209 | `kmpc_realloc` | `0x3CC0` | 160 | UnwindData |  |
| 2247 | `__kmpc_atomic_1` | `0x3E00` | 143 | UnwindData |  |
| 2251 | `__kmpc_atomic_10` | `0x3E90` | 77 | UnwindData |  |
| 2252 | `__kmpc_atomic_16` | `0x3EE0` | 77 | UnwindData |  |
| 2248 | `__kmpc_atomic_2` | `0x3F30` | 145 | UnwindData |  |
| 2253 | `__kmpc_atomic_20` | `0x3FD0` | 77 | UnwindData |  |
| 2254 | `__kmpc_atomic_32` | `0x4020` | 77 | UnwindData |  |
| 100 | `__kmpc_atomic_4` | `0x4070` | 140 | UnwindData |  |
| 101 | `__kmpc_atomic_8` | `0x4100` | 143 | UnwindData |  |
| 2143 | `__kmpc_atomic_bool_1_cas` | `0x4190` | 32 | UnwindData |  |
| 2151 | `__kmpc_atomic_bool_1_cas_cpt` | `0x41B0` | 58 | UnwindData |  |
| 2144 | `__kmpc_atomic_bool_2_cas` | `0x41F0` | 33 | UnwindData |  |
| 2152 | `__kmpc_atomic_bool_2_cas_cpt` | `0x4220` | 60 | UnwindData |  |
| 2145 | `__kmpc_atomic_bool_4_cas` | `0x4260` | 30 | UnwindData |  |
| 2153 | `__kmpc_atomic_bool_4_cas_cpt` | `0x4280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2146 | `__kmpc_atomic_bool_8_cas` | `0x42A0` | 30 | UnwindData |  |
| 2154 | `__kmpc_atomic_bool_8_cas_cpt` | `0x42C0` | 57 | UnwindData |  |
| 2093 | `__kmpc_atomic_cmplx10_add` | `0x4300` | 77 | UnwindData |  |
| 2391 | `__kmpc_atomic_cmplx10_add_cpt` | `0x4350` | 143 | UnwindData |  |
| 2096 | `__kmpc_atomic_cmplx10_div` | `0x43E0` | 157 | UnwindData |  |
| 2394 | `__kmpc_atomic_cmplx10_div_cpt` | `0x4480` | 259 | UnwindData |  |
| 2463 | `__kmpc_atomic_cmplx10_div_cpt_rev` | `0x4590` | 247 | UnwindData |  |
| 2507 | `__kmpc_atomic_cmplx10_div_rev` | `0x4690` | 157 | UnwindData |  |
| 2095 | `__kmpc_atomic_cmplx10_mul` | `0x4730` | 114 | UnwindData |  |
| 2393 | `__kmpc_atomic_cmplx10_mul_cpt` | `0x47B0` | 215 | UnwindData |  |
| 2275 | `__kmpc_atomic_cmplx10_rd` | `0x4890` | 87 | UnwindData |  |
| 2094 | `__kmpc_atomic_cmplx10_sub` | `0x48F0` | 77 | UnwindData |  |
| 2392 | `__kmpc_atomic_cmplx10_sub_cpt` | `0x4940` | 163 | UnwindData |  |
| 2462 | `__kmpc_atomic_cmplx10_sub_cpt_rev` | `0x49F0` | 143 | UnwindData |  |
| 2506 | `__kmpc_atomic_cmplx10_sub_rev` | `0x4A80` | 77 | UnwindData |  |
| 2422 | `__kmpc_atomic_cmplx10_swp` | `0x4AD0` | 98 | UnwindData |  |
| 2289 | `__kmpc_atomic_cmplx10_wr` | `0x4B40` | 70 | UnwindData |  |
| 2085 | `__kmpc_atomic_cmplx4_add` | `0x4B90` | 243 | UnwindData |  |
| 2231 | `__kmpc_atomic_cmplx4_add_cmplx8` | `0x4C90` | 274 | UnwindData |  |
| 2383 | `__kmpc_atomic_cmplx4_add_cpt` | `0x4DB0` | 154 | UnwindData |  |
| 2088 | `__kmpc_atomic_cmplx4_div` | `0x4E50` | 353 | UnwindData |  |
| 2234 | `__kmpc_atomic_cmplx4_div_cmplx8` | `0x4FC0` | 379 | UnwindData |  |
| 2386 | `__kmpc_atomic_cmplx4_div_cpt` | `0x5140` | 263 | UnwindData |  |
| 2459 | `__kmpc_atomic_cmplx4_div_cpt_rev` | `0x5250` | 259 | UnwindData |  |
| 2503 | `__kmpc_atomic_cmplx4_div_rev` | `0x5360` | 150 | UnwindData |  |
| 2087 | `__kmpc_atomic_cmplx4_mul` | `0x5400` | 300 | UnwindData |  |
| 2233 | `__kmpc_atomic_cmplx4_mul_cmplx8` | `0x5530` | 334 | UnwindData |  |
| 2385 | `__kmpc_atomic_cmplx4_mul_cpt` | `0x5680` | 210 | UnwindData |  |
| 2273 | `__kmpc_atomic_cmplx4_rd` | `0x5760` | 76 | UnwindData |  |
| 2086 | `__kmpc_atomic_cmplx4_sub` | `0x57B0` | 245 | UnwindData |  |
| 2232 | `__kmpc_atomic_cmplx4_sub_cmplx8` | `0x58B0` | 274 | UnwindData |  |
| 2384 | `__kmpc_atomic_cmplx4_sub_cpt` | `0x59D0` | 162 | UnwindData |  |
| 2458 | `__kmpc_atomic_cmplx4_sub_cpt_rev` | `0x5A80` | 151 | UnwindData |  |
| 2502 | `__kmpc_atomic_cmplx4_sub_rev` | `0x5B20` | 96 | UnwindData |  |
| 2420 | `__kmpc_atomic_cmplx4_swp` | `0x5B80` | 83 | UnwindData |  |
| 2287 | `__kmpc_atomic_cmplx4_wr` | `0x5BE0` | 70 | UnwindData |  |
| 2089 | `__kmpc_atomic_cmplx8_add` | `0x5C30` | 77 | UnwindData |  |
| 2387 | `__kmpc_atomic_cmplx8_add_cpt` | `0x5C80` | 143 | UnwindData |  |
| 2092 | `__kmpc_atomic_cmplx8_div` | `0x5D10` | 157 | UnwindData |  |
| 2390 | `__kmpc_atomic_cmplx8_div_cpt` | `0x5DB0` | 259 | UnwindData |  |
| 2461 | `__kmpc_atomic_cmplx8_div_cpt_rev` | `0x5EC0` | 247 | UnwindData |  |
| 2505 | `__kmpc_atomic_cmplx8_div_rev` | `0x5FC0` | 157 | UnwindData |  |
| 2091 | `__kmpc_atomic_cmplx8_mul` | `0x6060` | 114 | UnwindData |  |
| 2389 | `__kmpc_atomic_cmplx8_mul_cpt` | `0x60E0` | 215 | UnwindData |  |
| 2274 | `__kmpc_atomic_cmplx8_rd` | `0x61C0` | 87 | UnwindData |  |
| 2090 | `__kmpc_atomic_cmplx8_sub` | `0x6220` | 77 | UnwindData |  |
| 2388 | `__kmpc_atomic_cmplx8_sub_cpt` | `0x6270` | 163 | UnwindData |  |
| 2460 | `__kmpc_atomic_cmplx8_sub_cpt_rev` | `0x6320` | 143 | UnwindData |  |
| 2504 | `__kmpc_atomic_cmplx8_sub_rev` | `0x63B0` | 77 | UnwindData |  |
| 2421 | `__kmpc_atomic_cmplx8_swp` | `0x6400` | 98 | UnwindData |  |
| 2288 | `__kmpc_atomic_cmplx8_wr` | `0x6470` | 70 | UnwindData |  |
| 2411 | `__kmpc_atomic_end` | `0x64C0` | 27 | UnwindData |  |
| 2001 | `__kmpc_atomic_fixed1_add` | `0x64E0` | 78 | UnwindData |  |
| 2293 | `__kmpc_atomic_fixed1_add_cpt` | `0x6530` | 123 | UnwindData |  |
| 2002 | `__kmpc_atomic_fixed1_andb` | `0x65B0` | 81 | UnwindData |  |
| 2294 | `__kmpc_atomic_fixed1_andb_cpt` | `0x6610` | 127 | UnwindData |  |
| 2053 | `__kmpc_atomic_fixed1_andl` | `0x6690` | 93 | UnwindData |  |
| 2345 | `__kmpc_atomic_fixed1_andl_cpt` | `0x66F0` | 137 | UnwindData |  |
| 2003 | `__kmpc_atomic_fixed1_div` | `0x6780` | 85 | UnwindData |  |
| 2295 | `__kmpc_atomic_fixed1_div_cpt` | `0x67E0` | 126 | UnwindData |  |
| 2427 | `__kmpc_atomic_fixed1_div_cpt_rev` | `0x6860` | 126 | UnwindData |  |
| 2170 | `__kmpc_atomic_fixed1_div_float8` | `0x68E0` | 93 | UnwindData |  |
| 2471 | `__kmpc_atomic_fixed1_div_rev` | `0x6940` | 113 | UnwindData |  |
| 2077 | `__kmpc_atomic_fixed1_eqv` | `0x69C0` | 81 | UnwindData |  |
| 2371 | `__kmpc_atomic_fixed1_eqv_cpt` | `0x6A20` | 127 | UnwindData |  |
| 2061 | `__kmpc_atomic_fixed1_max` | `0x6AA0` | 94 | UnwindData |  |
| 2353 | `__kmpc_atomic_fixed1_max_cpt` | `0x6B00` | 30 | UnwindData |  |
| 2062 | `__kmpc_atomic_fixed1_min` | `0x6B70` | 94 | UnwindData |  |
| 2354 | `__kmpc_atomic_fixed1_min_cpt` | `0x6BD0` | 30 | UnwindData |  |
| 2005 | `__kmpc_atomic_fixed1_mul` | `0x6C40` | 81 | UnwindData |  |
| 2297 | `__kmpc_atomic_fixed1_mul_cpt` | `0x6CA0` | 125 | UnwindData |  |
| 2169 | `__kmpc_atomic_fixed1_mul_float8` | `0x6D20` | 93 | UnwindData |  |
| 2073 | `__kmpc_atomic_fixed1_neqv` | `0x6D80` | 81 | UnwindData |  |
| 2367 | `__kmpc_atomic_fixed1_neqv_cpt` | `0x6DE0` | 127 | UnwindData |  |
| 2006 | `__kmpc_atomic_fixed1_orb` | `0x6E60` | 81 | UnwindData |  |
| 2298 | `__kmpc_atomic_fixed1_orb_cpt` | `0x6EC0` | 127 | UnwindData |  |
| 2054 | `__kmpc_atomic_fixed1_orl` | `0x6F40` | 93 | UnwindData |  |
| 2346 | `__kmpc_atomic_fixed1_orl_cpt` | `0x6FA0` | 137 | UnwindData |  |
| 2265 | `__kmpc_atomic_fixed1_rd` | `0x7030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2007 | `__kmpc_atomic_fixed1_shl` | `0x7050` | 83 | UnwindData |  |
| 2299 | `__kmpc_atomic_fixed1_shl_cpt` | `0x70B0` | 128 | UnwindData |  |
| 2429 | `__kmpc_atomic_fixed1_shl_cpt_rev` | `0x7130` | 130 | UnwindData |  |
| 2473 | `__kmpc_atomic_fixed1_shl_rev` | `0x71C0` | 109 | UnwindData |  |
| 2008 | `__kmpc_atomic_fixed1_shr` | `0x7230` | 85 | UnwindData |  |
| 2300 | `__kmpc_atomic_fixed1_shr_cpt` | `0x7290` | 130 | UnwindData |  |
| 2430 | `__kmpc_atomic_fixed1_shr_cpt_rev` | `0x7320` | 130 | UnwindData |  |
| 2474 | `__kmpc_atomic_fixed1_shr_rev` | `0x73B0` | 109 | UnwindData |  |
| 2010 | `__kmpc_atomic_fixed1_sub` | `0x7420` | 81 | UnwindData |  |
| 2302 | `__kmpc_atomic_fixed1_sub_cpt` | `0x7480` | 127 | UnwindData |  |
| 2426 | `__kmpc_atomic_fixed1_sub_cpt_rev` | `0x7500` | 127 | UnwindData |  |
| 2470 | `__kmpc_atomic_fixed1_sub_rev` | `0x7580` | 91 | UnwindData |  |
| 2412 | `__kmpc_atomic_fixed1_swp` | `0x75E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2279 | `__kmpc_atomic_fixed1_wr` | `0x75F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2011 | `__kmpc_atomic_fixed1_xor` | `0x7600` | 81 | UnwindData |  |
| 2303 | `__kmpc_atomic_fixed1_xor_cpt` | `0x7660` | 127 | UnwindData |  |
| 2004 | `__kmpc_atomic_fixed1u_div` | `0x76E0` | 86 | UnwindData |  |
| 2296 | `__kmpc_atomic_fixed1u_div_cpt` | `0x7740` | 127 | UnwindData |  |
| 2428 | `__kmpc_atomic_fixed1u_div_cpt_rev` | `0x77C0` | 127 | UnwindData |  |
| 2472 | `__kmpc_atomic_fixed1u_div_rev` | `0x7840` | 114 | UnwindData |  |
| 2009 | `__kmpc_atomic_fixed1u_shr` | `0x78C0` | 85 | UnwindData |  |
| 2301 | `__kmpc_atomic_fixed1u_shr_cpt` | `0x7920` | 130 | UnwindData |  |
| 2431 | `__kmpc_atomic_fixed1u_shr_cpt_rev` | `0x79B0` | 130 | UnwindData |  |
| 2475 | `__kmpc_atomic_fixed1u_shr_rev` | `0x7A40` | 109 | UnwindData |  |
| 2012 | `__kmpc_atomic_fixed2_add` | `0x7AB0` | 79 | UnwindData |  |
| 2304 | `__kmpc_atomic_fixed2_add_cpt` | `0x7B00` | 121 | UnwindData |  |
| 2013 | `__kmpc_atomic_fixed2_andb` | `0x7B80` | 83 | UnwindData |  |
| 2305 | `__kmpc_atomic_fixed2_andb_cpt` | `0x7BE0` | 124 | UnwindData |  |
| 2055 | `__kmpc_atomic_fixed2_andl` | `0x7C60` | 115 | UnwindData |  |
| 2347 | `__kmpc_atomic_fixed2_andl_cpt` | `0x7CE0` | 181 | UnwindData |  |
| 2014 | `__kmpc_atomic_fixed2_div` | `0x7DA0` | 86 | UnwindData |  |
| 2306 | `__kmpc_atomic_fixed2_div_cpt` | `0x7E00` | 125 | UnwindData |  |
| 2433 | `__kmpc_atomic_fixed2_div_cpt_rev` | `0x7E80` | 125 | UnwindData |  |
| 2175 | `__kmpc_atomic_fixed2_div_float8` | `0x7F00` | 108 | UnwindData |  |
| 2477 | `__kmpc_atomic_fixed2_div_rev` | `0x7F70` | 115 | UnwindData |  |
| 2078 | `__kmpc_atomic_fixed2_eqv` | `0x7FF0` | 83 | UnwindData |  |
| 2372 | `__kmpc_atomic_fixed2_eqv_cpt` | `0x8050` | 124 | UnwindData |  |
| 2063 | `__kmpc_atomic_fixed2_max` | `0x80D0` | 97 | UnwindData |  |
| 2355 | `__kmpc_atomic_fixed2_max_cpt` | `0x8140` | 32 | UnwindData |  |
| 2064 | `__kmpc_atomic_fixed2_min` | `0x81C0` | 97 | UnwindData |  |
| 2356 | `__kmpc_atomic_fixed2_min_cpt` | `0x8230` | 32 | UnwindData |  |
| 2016 | `__kmpc_atomic_fixed2_mul` | `0x82B0` | 82 | UnwindData |  |
| 2308 | `__kmpc_atomic_fixed2_mul_cpt` | `0x8310` | 123 | UnwindData |  |
| 2174 | `__kmpc_atomic_fixed2_mul_float8` | `0x8390` | 108 | UnwindData |  |
| 2074 | `__kmpc_atomic_fixed2_neqv` | `0x8400` | 83 | UnwindData |  |
| 2368 | `__kmpc_atomic_fixed2_neqv_cpt` | `0x8460` | 124 | UnwindData |  |
| 2017 | `__kmpc_atomic_fixed2_orb` | `0x84E0` | 83 | UnwindData |  |
| 2309 | `__kmpc_atomic_fixed2_orb_cpt` | `0x8540` | 124 | UnwindData |  |
| 2056 | `__kmpc_atomic_fixed2_orl` | `0x85C0` | 115 | UnwindData |  |
| 2348 | `__kmpc_atomic_fixed2_orl_cpt` | `0x8640` | 181 | UnwindData |  |
| 2266 | `__kmpc_atomic_fixed2_rd` | `0x8700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2018 | `__kmpc_atomic_fixed2_shl` | `0x8720` | 85 | UnwindData |  |
| 2310 | `__kmpc_atomic_fixed2_shl_cpt` | `0x8780` | 126 | UnwindData |  |
| 2435 | `__kmpc_atomic_fixed2_shl_cpt_rev` | `0x8800` | 128 | UnwindData |  |
| 2479 | `__kmpc_atomic_fixed2_shl_rev` | `0x8880` | 112 | UnwindData |  |
| 2019 | `__kmpc_atomic_fixed2_shr` | `0x88F0` | 86 | UnwindData |  |
| 2311 | `__kmpc_atomic_fixed2_shr_cpt` | `0x8950` | 127 | UnwindData |  |
| 2436 | `__kmpc_atomic_fixed2_shr_cpt_rev` | `0x89D0` | 127 | UnwindData |  |
| 2480 | `__kmpc_atomic_fixed2_shr_rev` | `0x8A50` | 112 | UnwindData |  |
| 2021 | `__kmpc_atomic_fixed2_sub` | `0x8AC0` | 83 | UnwindData |  |
| 2313 | `__kmpc_atomic_fixed2_sub_cpt` | `0x8B20` | 124 | UnwindData |  |
| 2432 | `__kmpc_atomic_fixed2_sub_cpt_rev` | `0x8BA0` | 124 | UnwindData |  |
| 2476 | `__kmpc_atomic_fixed2_sub_rev` | `0x8C20` | 109 | UnwindData |  |
| 2413 | `__kmpc_atomic_fixed2_swp` | `0x8C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2280 | `__kmpc_atomic_fixed2_wr` | `0x8CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2022 | `__kmpc_atomic_fixed2_xor` | `0x8CB0` | 83 | UnwindData |  |
| 2314 | `__kmpc_atomic_fixed2_xor_cpt` | `0x8D10` | 124 | UnwindData |  |
| 2015 | `__kmpc_atomic_fixed2u_div` | `0x8D90` | 87 | UnwindData |  |
| 2307 | `__kmpc_atomic_fixed2u_div_cpt` | `0x8DF0` | 126 | UnwindData |  |
| 2434 | `__kmpc_atomic_fixed2u_div_cpt_rev` | `0x8E70` | 126 | UnwindData |  |
| 2478 | `__kmpc_atomic_fixed2u_div_rev` | `0x8EF0` | 116 | UnwindData |  |
| 2020 | `__kmpc_atomic_fixed2u_shr` | `0x8F70` | 86 | UnwindData |  |
| 2312 | `__kmpc_atomic_fixed2u_shr_cpt` | `0x8FD0` | 127 | UnwindData |  |
| 2437 | `__kmpc_atomic_fixed2u_shr_cpt_rev` | `0x9050` | 127 | UnwindData |  |
| 2481 | `__kmpc_atomic_fixed2u_shr_rev` | `0x90D0` | 112 | UnwindData |  |
| 102 | `__kmpc_atomic_fixed4_add` | `0x9140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2315 | `__kmpc_atomic_fixed4_add_cpt` | `0x9150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2031 | `__kmpc_atomic_fixed4_andb` | `0x9170` | 79 | UnwindData |  |
| 2323 | `__kmpc_atomic_fixed4_andb_cpt` | `0x91C0` | 98 | UnwindData |  |
| 2057 | `__kmpc_atomic_fixed4_andl` | `0x9230` | 95 | UnwindData |  |
| 2349 | `__kmpc_atomic_fixed4_andl_cpt` | `0x9290` | 127 | UnwindData |  |
| 2032 | `__kmpc_atomic_fixed4_div` | `0x9310` | 83 | UnwindData |  |
| 2324 | `__kmpc_atomic_fixed4_div_cpt` | `0x9370` | 100 | UnwindData |  |
| 2439 | `__kmpc_atomic_fixed4_div_cpt_rev` | `0x93E0` | 117 | UnwindData |  |
| 2180 | `__kmpc_atomic_fixed4_div_float8` | `0x9460` | 91 | UnwindData |  |
| 2483 | `__kmpc_atomic_fixed4_div_rev` | `0x94C0` | 93 | UnwindData |  |
| 2079 | `__kmpc_atomic_fixed4_eqv` | `0x9520` | 79 | UnwindData |  |
| 2373 | `__kmpc_atomic_fixed4_eqv_cpt` | `0x9570` | 99 | UnwindData |  |
| 2065 | `__kmpc_atomic_fixed4_max` | `0x95E0` | 90 | UnwindData |  |
| 2357 | `__kmpc_atomic_fixed4_max_cpt` | `0x9640` | 28 | UnwindData |  |
| 2066 | `__kmpc_atomic_fixed4_min` | `0x96B0` | 90 | UnwindData |  |
| 2358 | `__kmpc_atomic_fixed4_min_cpt` | `0x9710` | 28 | UnwindData |  |
| 2034 | `__kmpc_atomic_fixed4_mul` | `0x9780` | 80 | UnwindData |  |
| 2326 | `__kmpc_atomic_fixed4_mul_cpt` | `0x97D0` | 100 | UnwindData |  |
| 2179 | `__kmpc_atomic_fixed4_mul_float8` | `0x9840` | 91 | UnwindData |  |
| 2075 | `__kmpc_atomic_fixed4_neqv` | `0x98A0` | 79 | UnwindData |  |
| 2369 | `__kmpc_atomic_fixed4_neqv_cpt` | `0x98F0` | 98 | UnwindData |  |
| 2035 | `__kmpc_atomic_fixed4_orb` | `0x9960` | 79 | UnwindData |  |
| 2327 | `__kmpc_atomic_fixed4_orb_cpt` | `0x99B0` | 98 | UnwindData |  |
| 2058 | `__kmpc_atomic_fixed4_orl` | `0x9A20` | 95 | UnwindData |  |
| 2350 | `__kmpc_atomic_fixed4_orl_cpt` | `0x9A80` | 127 | UnwindData |  |
| 2267 | `__kmpc_atomic_fixed4_rd` | `0x9B00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2036 | `__kmpc_atomic_fixed4_shl` | `0x9B10` | 81 | UnwindData |  |
| 2328 | `__kmpc_atomic_fixed4_shl_cpt` | `0x9B70` | 102 | UnwindData |  |
| 2441 | `__kmpc_atomic_fixed4_shl_cpt_rev` | `0x9BE0` | 102 | UnwindData |  |
| 2485 | `__kmpc_atomic_fixed4_shl_rev` | `0x9C50` | 89 | UnwindData |  |
| 2037 | `__kmpc_atomic_fixed4_shr` | `0x9CB0` | 81 | UnwindData |  |
| 2329 | `__kmpc_atomic_fixed4_shr_cpt` | `0x9D10` | 102 | UnwindData |  |
| 2442 | `__kmpc_atomic_fixed4_shr_cpt_rev` | `0x9D80` | 102 | UnwindData |  |
| 2486 | `__kmpc_atomic_fixed4_shr_rev` | `0x9DF0` | 89 | UnwindData |  |
| 2024 | `__kmpc_atomic_fixed4_sub` | `0x9E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2316 | `__kmpc_atomic_fixed4_sub_cpt` | `0x9E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2438 | `__kmpc_atomic_fixed4_sub_cpt_rev` | `0x9E80` | 98 | UnwindData |  |
| 2482 | `__kmpc_atomic_fixed4_sub_rev` | `0x9EF0` | 87 | UnwindData |  |
| 2414 | `__kmpc_atomic_fixed4_swp` | `0x9F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2281 | `__kmpc_atomic_fixed4_wr` | `0x9F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2039 | `__kmpc_atomic_fixed4_xor` | `0x9F70` | 79 | UnwindData |  |
| 2331 | `__kmpc_atomic_fixed4_xor_cpt` | `0x9FC0` | 98 | UnwindData |  |
| 2033 | `__kmpc_atomic_fixed4u_div` | `0xA030` | 84 | UnwindData |  |
| 2325 | `__kmpc_atomic_fixed4u_div_cpt` | `0xA090` | 116 | UnwindData |  |
| 2440 | `__kmpc_atomic_fixed4u_div_cpt_rev` | `0xA110` | 118 | UnwindData |  |
| 2484 | `__kmpc_atomic_fixed4u_div_rev` | `0xA190` | 108 | UnwindData |  |
| 2038 | `__kmpc_atomic_fixed4u_shr` | `0xA200` | 81 | UnwindData |  |
| 2330 | `__kmpc_atomic_fixed4u_shr_cpt` | `0xA260` | 102 | UnwindData |  |
| 2443 | `__kmpc_atomic_fixed4u_shr_cpt_rev` | `0xA2D0` | 102 | UnwindData |  |
| 2487 | `__kmpc_atomic_fixed4u_shr_rev` | `0xA340` | 89 | UnwindData |  |
| 103 | `__kmpc_atomic_fixed8_add` | `0xA3A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2319 | `__kmpc_atomic_fixed8_add_cpt` | `0xA3B0` | 36 | UnwindData |  |
| 2040 | `__kmpc_atomic_fixed8_andb` | `0xA3E0` | 80 | UnwindData |  |
| 2332 | `__kmpc_atomic_fixed8_andb_cpt` | `0xA430` | 122 | UnwindData |  |
| 2059 | `__kmpc_atomic_fixed8_andl` | `0xA4B0` | 99 | UnwindData |  |
| 2351 | `__kmpc_atomic_fixed8_andl_cpt` | `0xA520` | 151 | UnwindData |  |
| 2041 | `__kmpc_atomic_fixed8_div` | `0xA5C0` | 88 | UnwindData |  |
| 2333 | `__kmpc_atomic_fixed8_div_cpt` | `0xA620` | 124 | UnwindData |  |
| 2445 | `__kmpc_atomic_fixed8_div_cpt_rev` | `0xA6A0` | 127 | UnwindData |  |
| 2185 | `__kmpc_atomic_fixed8_div_float8` | `0xA720` | 92 | UnwindData |  |
| 2489 | `__kmpc_atomic_fixed8_div_rev` | `0xA780` | 114 | UnwindData |  |
| 2080 | `__kmpc_atomic_fixed8_eqv` | `0xA800` | 80 | UnwindData |  |
| 2374 | `__kmpc_atomic_fixed8_eqv_cpt` | `0xA850` | 122 | UnwindData |  |
| 2067 | `__kmpc_atomic_fixed8_max` | `0xA8D0` | 95 | UnwindData |  |
| 2359 | `__kmpc_atomic_fixed8_max_cpt` | `0xA930` | 29 | UnwindData |  |
| 2068 | `__kmpc_atomic_fixed8_min` | `0xA9A0` | 95 | UnwindData |  |
| 2360 | `__kmpc_atomic_fixed8_min_cpt` | `0xAA00` | 29 | UnwindData |  |
| 2043 | `__kmpc_atomic_fixed8_mul` | `0xAA70` | 81 | UnwindData |  |
| 2335 | `__kmpc_atomic_fixed8_mul_cpt` | `0xAAD0` | 123 | UnwindData |  |
| 2184 | `__kmpc_atomic_fixed8_mul_float8` | `0xAB50` | 92 | UnwindData |  |
| 2076 | `__kmpc_atomic_fixed8_neqv` | `0xABB0` | 80 | UnwindData |  |
| 2370 | `__kmpc_atomic_fixed8_neqv_cpt` | `0xAC00` | 122 | UnwindData |  |
| 2044 | `__kmpc_atomic_fixed8_orb` | `0xAC80` | 80 | UnwindData |  |
| 2336 | `__kmpc_atomic_fixed8_orb_cpt` | `0xACD0` | 122 | UnwindData |  |
| 2060 | `__kmpc_atomic_fixed8_orl` | `0xAD50` | 99 | UnwindData |  |
| 2352 | `__kmpc_atomic_fixed8_orl_cpt` | `0xADC0` | 151 | UnwindData |  |
| 2268 | `__kmpc_atomic_fixed8_rd` | `0xAE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2045 | `__kmpc_atomic_fixed8_shl` | `0xAE70` | 83 | UnwindData |  |
| 2337 | `__kmpc_atomic_fixed8_shl_cpt` | `0xAED0` | 125 | UnwindData |  |
| 2447 | `__kmpc_atomic_fixed8_shl_cpt_rev` | `0xAF50` | 125 | UnwindData |  |
| 2491 | `__kmpc_atomic_fixed8_shl_rev` | `0xAFD0` | 109 | UnwindData |  |
| 2046 | `__kmpc_atomic_fixed8_shr` | `0xB040` | 83 | UnwindData |  |
| 2338 | `__kmpc_atomic_fixed8_shr_cpt` | `0xB0A0` | 125 | UnwindData |  |
| 2448 | `__kmpc_atomic_fixed8_shr_cpt_rev` | `0xB120` | 125 | UnwindData |  |
| 2492 | `__kmpc_atomic_fixed8_shr_rev` | `0xB1A0` | 109 | UnwindData |  |
| 2028 | `__kmpc_atomic_fixed8_sub` | `0xB210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2320 | `__kmpc_atomic_fixed8_sub_cpt` | `0xB220` | 44 | UnwindData |  |
| 2444 | `__kmpc_atomic_fixed8_sub_cpt_rev` | `0xB250` | 122 | UnwindData |  |
| 2488 | `__kmpc_atomic_fixed8_sub_rev` | `0xB2D0` | 90 | UnwindData |  |
| 2415 | `__kmpc_atomic_fixed8_swp` | `0xB330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2282 | `__kmpc_atomic_fixed8_wr` | `0xB340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2048 | `__kmpc_atomic_fixed8_xor` | `0xB350` | 80 | UnwindData |  |
| 2340 | `__kmpc_atomic_fixed8_xor_cpt` | `0xB3A0` | 122 | UnwindData |  |
| 2042 | `__kmpc_atomic_fixed8u_div` | `0xB420` | 88 | UnwindData |  |
| 2334 | `__kmpc_atomic_fixed8u_div_cpt` | `0xB480` | 124 | UnwindData |  |
| 2446 | `__kmpc_atomic_fixed8u_div_cpt_rev` | `0xB500` | 127 | UnwindData |  |
| 2490 | `__kmpc_atomic_fixed8u_div_rev` | `0xB580` | 114 | UnwindData |  |
| 2047 | `__kmpc_atomic_fixed8u_shr` | `0xB600` | 83 | UnwindData |  |
| 2339 | `__kmpc_atomic_fixed8u_shr_cpt` | `0xB660` | 125 | UnwindData |  |
| 2449 | `__kmpc_atomic_fixed8u_shr_cpt_rev` | `0xB6E0` | 125 | UnwindData |  |
| 2493 | `__kmpc_atomic_fixed8u_shr_rev` | `0xB760` | 109 | UnwindData |  |
| 2081 | `__kmpc_atomic_float10_add` | `0xB7D0` | 72 | UnwindData |  |
| 2375 | `__kmpc_atomic_float10_add_cpt` | `0xB820` | 103 | UnwindData |  |
| 2084 | `__kmpc_atomic_float10_div` | `0xB890` | 76 | UnwindData |  |
| 2378 | `__kmpc_atomic_float10_div_cpt` | `0xB8E0` | 103 | UnwindData |  |
| 2455 | `__kmpc_atomic_float10_div_cpt_rev` | `0xB950` | 100 | UnwindData |  |
| 2499 | `__kmpc_atomic_float10_div_rev` | `0xB9C0` | 72 | UnwindData |  |
| 2139 | `__kmpc_atomic_float10_max` | `0xBA10` | 82 | UnwindData |  |
| 2141 | `__kmpc_atomic_float10_max_cpt` | `0xBA70` | 103 | UnwindData |  |
| 2140 | `__kmpc_atomic_float10_min` | `0xBAE0` | 90 | UnwindData |  |
| 2142 | `__kmpc_atomic_float10_min_cpt` | `0xBB40` | 103 | UnwindData |  |
| 2083 | `__kmpc_atomic_float10_mul` | `0xBBB0` | 72 | UnwindData |  |
| 2377 | `__kmpc_atomic_float10_mul_cpt` | `0xBC00` | 103 | UnwindData |  |
| 2271 | `__kmpc_atomic_float10_rd` | `0xBC70` | 69 | UnwindData |  |
| 2082 | `__kmpc_atomic_float10_sub` | `0xBCC0` | 76 | UnwindData |  |
| 2376 | `__kmpc_atomic_float10_sub_cpt` | `0xBD10` | 103 | UnwindData |  |
| 2454 | `__kmpc_atomic_float10_sub_cpt_rev` | `0xBD80` | 100 | UnwindData |  |
| 2498 | `__kmpc_atomic_float10_sub_rev` | `0xBDF0` | 72 | UnwindData |  |
| 2418 | `__kmpc_atomic_float10_swp` | `0xBE40` | 86 | UnwindData |  |
| 2285 | `__kmpc_atomic_float10_wr` | `0xBEA0` | 68 | UnwindData |  |
| 104 | `__kmpc_atomic_float4_add` | `0xBEF0` | 93 | UnwindData |  |
| 2317 | `__kmpc_atomic_float4_add_cpt` | `0xBF50` | 165 | UnwindData |  |
| 2187 | `__kmpc_atomic_float4_add_float8` | `0xC000` | 111 | UnwindData |  |
| 2049 | `__kmpc_atomic_float4_div` | `0xC070` | 93 | UnwindData |  |
| 2341 | `__kmpc_atomic_float4_div_cpt` | `0xC0D0` | 165 | UnwindData |  |
| 2451 | `__kmpc_atomic_float4_div_cpt_rev` | `0xC180` | 165 | UnwindData |  |
| 2190 | `__kmpc_atomic_float4_div_float8` | `0xC230` | 111 | UnwindData |  |
| 2495 | `__kmpc_atomic_float4_div_rev` | `0xC2A0` | 119 | UnwindData |  |
| 2069 | `__kmpc_atomic_float4_max` | `0xC320` | 50 | UnwindData |  |
| 2361 | `__kmpc_atomic_float4_max_cpt` | `0xC3A0` | 33 | UnwindData |  |
| 2070 | `__kmpc_atomic_float4_min` | `0xC440` | 49 | UnwindData |  |
| 2362 | `__kmpc_atomic_float4_min_cpt` | `0xC4C0` | 33 | UnwindData |  |
| 2050 | `__kmpc_atomic_float4_mul` | `0xC560` | 93 | UnwindData |  |
| 2342 | `__kmpc_atomic_float4_mul_cpt` | `0xC5C0` | 165 | UnwindData |  |
| 2189 | `__kmpc_atomic_float4_mul_float8` | `0xC670` | 111 | UnwindData |  |
| 2269 | `__kmpc_atomic_float4_rd` | `0xC6E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2026 | `__kmpc_atomic_float4_sub` | `0xC710` | 93 | UnwindData |  |
| 2318 | `__kmpc_atomic_float4_sub_cpt` | `0xC770` | 165 | UnwindData |  |
| 2450 | `__kmpc_atomic_float4_sub_cpt_rev` | `0xC820` | 165 | UnwindData |  |
| 2188 | `__kmpc_atomic_float4_sub_float8` | `0xC8D0` | 111 | UnwindData |  |
| 2494 | `__kmpc_atomic_float4_sub_rev` | `0xC940` | 119 | UnwindData |  |
| 2416 | `__kmpc_atomic_float4_swp` | `0xC9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2283 | `__kmpc_atomic_float4_wr` | `0xC9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `__kmpc_atomic_float8_add` | `0xC9E0` | 108 | UnwindData |  |
| 2321 | `__kmpc_atomic_float8_add_cpt` | `0xCA50` | 166 | UnwindData |  |
| 2051 | `__kmpc_atomic_float8_div` | `0xCB00` | 108 | UnwindData |  |
| 2343 | `__kmpc_atomic_float8_div_cpt` | `0xCB70` | 166 | UnwindData |  |
| 2453 | `__kmpc_atomic_float8_div_cpt_rev` | `0xCC20` | 166 | UnwindData |  |
| 2497 | `__kmpc_atomic_float8_div_rev` | `0xCCD0` | 120 | UnwindData |  |
| 2071 | `__kmpc_atomic_float8_max` | `0xCD50` | 52 | UnwindData |  |
| 2363 | `__kmpc_atomic_float8_max_cpt` | `0xCDD0` | 34 | UnwindData |  |
| 2072 | `__kmpc_atomic_float8_min` | `0xCE70` | 51 | UnwindData |  |
| 2364 | `__kmpc_atomic_float8_min_cpt` | `0xCEF0` | 34 | UnwindData |  |
| 2052 | `__kmpc_atomic_float8_mul` | `0xCF90` | 108 | UnwindData |  |
| 2344 | `__kmpc_atomic_float8_mul_cpt` | `0xD000` | 166 | UnwindData |  |
| 2270 | `__kmpc_atomic_float8_rd` | `0xD0B0` | 53 | UnwindData |  |
| 2030 | `__kmpc_atomic_float8_sub` | `0xD0F0` | 108 | UnwindData |  |
| 2322 | `__kmpc_atomic_float8_sub_cpt` | `0xD160` | 166 | UnwindData |  |
| 2452 | `__kmpc_atomic_float8_sub_cpt_rev` | `0xD210` | 166 | UnwindData |  |
| 2496 | `__kmpc_atomic_float8_sub_rev` | `0xD2C0` | 120 | UnwindData |  |
| 2417 | `__kmpc_atomic_float8_swp` | `0xD340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2284 | `__kmpc_atomic_float8_wr` | `0xD350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2410 | `__kmpc_atomic_start` | `0xD360` | 27 | UnwindData |  |
| 2147 | `__kmpc_atomic_val_1_cas` | `0xD380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2155 | `__kmpc_atomic_val_1_cas_cpt` | `0xD3A0` | 57 | UnwindData |  |
| 2148 | `__kmpc_atomic_val_2_cas` | `0xD3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2156 | `__kmpc_atomic_val_2_cas_cpt` | `0xD400` | 54 | UnwindData |  |
| 2149 | `__kmpc_atomic_val_4_cas` | `0xD440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2157 | `__kmpc_atomic_val_4_cas_cpt` | `0xD450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2150 | `__kmpc_atomic_val_8_cas` | `0xD470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2158 | `__kmpc_atomic_val_8_cas_cpt` | `0xD480` | 51 | UnwindData |  |
| 106 | `__kmpc_barrier` | `0xD630` | 64 | UnwindData |  |
| 107 | `__kmpc_barrier_master` | `0xD730` | 135 | UnwindData |  |
| 108 | `__kmpc_barrier_master_nowait` | `0xD7C0` | 65 | UnwindData |  |
| 110 | `__kmpc_begin` | `0xD940` | 71 | UnwindData |  |
| 111 | `__kmpc_bound_num_threads` | `0xD990` | 38 | UnwindData |  |
| 112 | `__kmpc_bound_thread_num` | `0xD9C0` | 31 | UnwindData |  |
| 172 | `__kmpc_copyprivate` | `0xD9E0` | 70 | UnwindData |  |
| 288 | `__kmpc_copyprivate_light` | `0xDB40` | 62 | UnwindData |  |
| 113 | `__kmpc_critical` | `0xDC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `__kmpc_critical_with_hint` | `0xDC50` | 6 | UnwindData |  |
| 176 | `__kmpc_destroy_lock` | `0xDF60` | 87 | UnwindData |  |
| 181 | `__kmpc_destroy_nest_lock` | `0xDFC0` | 65 | UnwindData |  |
| 264 | `__kmpc_doacross_fini` | `0xE010` | 49 | UnwindData |  |
| 261 | `__kmpc_doacross_init` | `0xE0D0` | 57 | UnwindData |  |
| 263 | `__kmpc_doacross_post` | `0xE350` | 54 | UnwindData |  |
| 262 | `__kmpc_doacross_wait` | `0xE480` | 55 | UnwindData |  |
| 120 | `__kmpc_end` | `0xE660` | 32 | UnwindData |  |
| 121 | `__kmpc_end_barrier_master` | `0xE680` | 29 | UnwindData |  |
| 123 | `__kmpc_end_critical` | `0xE6A0` | 252 | UnwindData |  |
| 283 | `__kmpc_end_masked` | `0xE7A0` | 57 | UnwindData |  |
| 124 | `__kmpc_end_master` | `0xE7E0` | 77 | UnwindData |  |
| 125 | `__kmpc_end_ordered` | `0xE830` | 150 | UnwindData |  |
| 190 | `__kmpc_end_reduce` | `0xE8D0` | 8 | UnwindData |  |
| 188 | `__kmpc_end_reduce_nowait` | `0xEB50` | 270 | UnwindData |  |
| 287 | `__kmpc_end_scope` | `0xEC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `__kmpc_end_serialized_parallel` | `0xEC70` | 24 | UnwindData |  |
| 127 | `__kmpc_end_single` | `0xEF00` | 27 | UnwindData |  |
| 281 | `__kmpc_error` | `0xEF20` | 19 | UnwindData |  |
| 130 | `__kmpc_flush` | `0xF0D0` | 44 | UnwindData |  |
| 135 | `__kmpc_for_static_fini` | `0xF100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `__kmpc_fork_call` | `0xF120` | 101 | UnwindData |  |
| 294 | `__kmpc_fork_call_if` | `0xF190` | 176 | UnwindData |  |
| 241 | `__kmpc_fork_teams` | `0xF240` | 254 | UnwindData |  |
| 234 | `__kmpc_get_parent_taskid` | `0xF340` | 66 | UnwindData |  |
| 271 | `__kmpc_get_target_offload` | `0xF390` | 30 | UnwindData |  |
| 233 | `__kmpc_get_taskid` | `0xF3B0` | 49 | UnwindData |  |
| 140 | `__kmpc_global_num_threads` | `0xF3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `__kmpc_global_thread_num` | `0xF400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `__kmpc_in_parallel` | `0xF410` | 34 | UnwindData |  |
| 175 | `__kmpc_init_lock` | `0xF440` | 271 | UnwindData |  |
| 180 | `__kmpc_init_nest_lock` | `0xF6C0` | 269 | UnwindData |  |
| 143 | `__kmpc_invoke_task_func` | `0xF930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `__kmpc_masked` | `0xF940` | 129 | UnwindData |  |
| 144 | `__kmpc_master` | `0xF9D0` | 146 | UnwindData |  |
| 145 | `__kmpc_ok_to_fork` | `0xFA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `__kmpc_ordered` | `0xFA80` | 226 | UnwindData |  |
| 273 | `__kmpc_pause_resource` | `0xFB70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `__kmpc_pop_num_threads` | `0xFB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `__kmpc_push_num_teams` | `0xFBA0` | 51 | UnwindData |  |
| 284 | `__kmpc_push_num_teams_51` | `0xFBE0` | 51 | UnwindData |  |
| 148 | `__kmpc_push_num_threads` | `0xFC20` | 58 | UnwindData |  |
| 170 | `__kmpc_push_num_threads_list` | `0xFC60` | 51 | UnwindData |  |
| 171 | `__kmpc_push_num_threads_list_strict` | `0xFCA0` | 50 | UnwindData |  |
| 173 | `__kmpc_push_num_threads_strict` | `0xFCE0` | 61 | UnwindData |  |
| 237 | `__kmpc_push_proc_bind` | `0xFD20` | 58 | UnwindData |  |
| 189 | `__kmpc_reduce` | `0xFD60` | 17 | UnwindData |  |
| 187 | `__kmpc_reduce_nowait` | `0x10180` | 17 | UnwindData |  |
| 286 | `__kmpc_scope` | `0x105B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `__kmpc_serialized_parallel` | `0x105C0` | 42 | UnwindData |  |
| 177 | `__kmpc_set_lock` | `0x105F0` | 197 | UnwindData |  |
| 182 | `__kmpc_set_nest_lock` | `0x106C0` | 182 | UnwindData |  |
| 186 | `__kmpc_set_thread_limit` | `0x10780` | 59 | UnwindData |  |
| 151 | `__kmpc_single` | `0x107C0` | 48 | UnwindData |  |
| 179 | `__kmpc_test_lock` | `0x107F0` | 284 | UnwindData |  |
| 184 | `__kmpc_test_nest_lock` | `0x10910` | 224 | UnwindData |  |
| 178 | `__kmpc_unset_lock` | `0x109F0` | 129 | UnwindData |  |
| 183 | `__kmpc_unset_nest_lock` | `0x10A80` | 115 | UnwindData |  |
| 860 | `kmpc_get_affinity_mask_proc` | `0x10B00` | 114 | UnwindData |  |
| 856 | `kmpc_set_affinity_mask_proc` | `0x10B80` | 114 | UnwindData |  |
| 211 | `kmpc_set_blocktime` | `0x10C00` | 92 | UnwindData |  |
| 224 | `kmpc_set_defaults` | `0x10D20` | 55 | UnwindData |  |
| 267 | `kmpc_set_disp_num_buffers` | `0x10D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `kmpc_set_library` | `0x10D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `kmpc_set_stacksize` | `0x10D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `kmpc_set_stacksize_s` | `0x10DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `kmpc_unset_affinity_mask_proc` | `0x10DB0` | 114 | UnwindData |  |
| 778 | `omp_aligned_alloc` | `0x10E30` | 60 | UnwindData |  |
| 806 | `omp_aligned_calloc` | `0x10E70` | 56 | UnwindData |  |
| 894 | `omp_alloc` | `0x10EB0` | 46 | UnwindData |  |
| 776 | `omp_calloc` | `0x10EE0` | 65 | UnwindData |  |
| 895 | `omp_free` | `0x10F30` | 44 | UnwindData |  |
| 777 | `omp_realloc` | `0x10F60` | 56 | UnwindData |  |
| 755 | `ompc_capture_affinity` | `0x10FA0` | 310 | UnwindData |  |
| 754 | `ompc_display_affinity` | `0x110E0` | 173 | UnwindData |  |
| 753 | `ompc_get_affinity_format` | `0x11190` | 90 | UnwindData |  |
| 800 | `ompc_get_ancestor_thread_num` | `0x11230` | 27 | UnwindData |  |
| 801 | `ompc_get_team_size` | `0x11250` | 27 | UnwindData |  |
| 752 | `ompc_set_affinity_format` | `0x11270` | 126 | UnwindData |  |
| 722 | `ompc_set_dynamic` | `0x112F0` | 65 | UnwindData |  |
| 798 | `ompc_set_max_active_levels` | `0x11340` | 27 | UnwindData |  |
| 723 | `ompc_set_nested` | `0x11360` | 74 | UnwindData |  |
| 724 | `ompc_set_num_threads` | `0x113B0` | 27 | UnwindData |  |
| 799 | `ompc_set_schedule` | `0x113D0` | 41 | UnwindData |  |
| 139 | `__kmp_fork_call` | `0x1B210` | 2,622 | UnwindData |  |
| 149 | `__kmp_get_reduce_method` | `0x1C740` | 37 | UnwindData |  |
| 239 | `__kmpc_end_taskgroup` | `0x368F0` | 264 | UnwindData |  |
| 272 | `__kmpc_omp_reg_task_with_affinity` | `0x36F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `__kmpc_omp_target_task_alloc` | `0x36F80` | 111 | UnwindData |  |
| 192 | `__kmpc_omp_task` | `0x36FF0` | 45 | UnwindData |  |
| 191 | `__kmpc_omp_task_alloc` | `0x37020` | 88 | UnwindData |  |
| 196 | `__kmpc_omp_task_begin_if0` | `0x37080` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `__kmpc_omp_task_complete_if0` | `0x370F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `__kmpc_omp_task_parts` | `0x37100` | 82 | UnwindData |  |
| 193 | `__kmpc_omp_taskwait` | `0x37160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `__kmpc_omp_taskyield` | `0x37170` | 70 | UnwindData |  |
| 259 | `__kmpc_proxy_task_completed` | `0x37530` | 153 | UnwindData |  |
| 260 | `__kmpc_proxy_task_completed_ooo` | `0x375D0` | 74 | UnwindData |  |
| 276 | `__kmpc_task_allow_completion_event` | `0x37620` | 45 | UnwindData |  |
| 269 | `__kmpc_task_reduction_get_th_data` | `0x37650` | 56 | UnwindData |  |
| 268 | `__kmpc_task_reduction_init` | `0x37810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `__kmpc_task_reduction_modifier_fini` | `0x37820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `__kmpc_task_reduction_modifier_init` | `0x37830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `__kmpc_taskgroup` | `0x37840` | 86 | UnwindData |  |
| 266 | `__kmpc_taskloop` | `0x378A0` | 147 | UnwindData |  |
| 285 | `__kmpc_taskloop_5` | `0x37940` | 51 | UnwindData |  |
| 277 | `__kmpc_taskred_init` | `0x37980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `__kmpc_taskred_modifier_init` | `0x37990` | 1,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `__kmpc_threadprivate` | `0x37E50` | 100 | UnwindData |  |
| 157 | `__kmpc_threadprivate_cached` | `0x38050` | 331 | UnwindData |  |
| 158 | `__kmpc_threadprivate_register` | `0x383B0` | 143 | UnwindData |  |
| 159 | `__kmpc_threadprivate_register_vec` | `0x38440` | 159 | UnwindData |  |
| 155 | `__kmp_release_64` | `0x3F6A0` | 151 | UnwindData |  |
| 161 | `__kmp_wait_64` | `0x3F740` | 95,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `__kmp_wait_4` | `0x56DA0` | 328 | UnwindData |  |
| 166 | `__kmpc_dispatch_deinit` | `0x57040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `__kmpc_dispatch_fini_4` | `0x57050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `__kmpc_dispatch_fini_4u` | `0x57060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `__kmpc_dispatch_fini_8` | `0x57070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `__kmpc_dispatch_fini_8u` | `0x57080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `__kmpc_dispatch_init_4` | `0x57090` | 49 | UnwindData |  |
| 230 | `__kmpc_dispatch_init_4u` | `0x570D0` | 49 | UnwindData |  |
| 117 | `__kmpc_dispatch_init_8` | `0x57110` | 55 | UnwindData |  |
| 226 | `__kmpc_dispatch_init_8u` | `0x57150` | 55 | UnwindData |  |
| 118 | `__kmpc_dispatch_next_4` | `0x57190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `__kmpc_dispatch_next_4u` | `0x571A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `__kmpc_dispatch_next_8` | `0x571B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `__kmpc_dispatch_next_8u` | `0x571C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `__kmpc_dist_dispatch_init_4` | `0x571D0` | 131 | UnwindData |  |
| 252 | `__kmpc_dist_dispatch_init_4u` | `0x57260` | 131 | UnwindData |  |
| 253 | `__kmpc_dist_dispatch_init_8` | `0x572F0` | 137 | UnwindData |  |
| 254 | `__kmpc_dist_dispatch_init_8u` | `0x57380` | 137 | UnwindData |  |
| 291 | `__kmpc_end_sections` | `0x57410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `__kmpc_next_section` | `0x57420` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `__kmpc_sections_init` | `0x57490` | 197 | UnwindData |  |
| 133 | `__kmp_acquire_tas_lock` | `0x5A6F0` | 74 | UnwindData |  |
| 129 | `__kmp_acquire_nested_tas_lock` | `0x5A9B0` | 91 | UnwindData |  |
| 109 | `__kmp_acquire_drdpa_lock` | `0x5AD90` | 524 | UnwindData |  |
| 122 | `__kmp_acquire_nested_drdpa_lock` | `0x5AFA0` | 612 | UnwindData |  |
| 128 | `__kmp_acquire_nested_queuing_lock` | `0x5B210` | 410 | UnwindData |  |
| 131 | `__kmp_acquire_nested_ticket_lock` | `0x5B3B0` | 109 | UnwindData |  |
| 132 | `__kmp_acquire_queuing_lock` | `0x5B420` | 353 | UnwindData |  |
| 134 | `__kmp_acquire_ticket_lock` | `0x5B590` | 53 | UnwindData |  |
| 247 | `__kmpc_dist_for_static_init_4` | `0x5F5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `__kmpc_dist_for_static_init_4u` | `0x5F5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `__kmpc_dist_for_static_init_8` | `0x5F5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `__kmpc_dist_for_static_init_8u` | `0x5F600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `__kmpc_for_static_init_4` | `0x5F610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `__kmpc_for_static_init_4u` | `0x5F620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `__kmpc_for_static_init_8` | `0x5F630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `__kmpc_for_static_init_8u` | `0x5F640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `__kmpc_team_static_init_4` | `0x5F650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `__kmpc_team_static_init_4u` | `0x5F660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `__kmpc_team_static_init_8` | `0x5F670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `__kmpc_team_static_init_8u` | `0x5F680` | 10,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `__kmpc_calc_original_ivs_rectang` | `0x62000` | 415 | UnwindData |  |
| 296 | `__kmpc_for_collapsed_init` | `0x621A0` | 1,675 | UnwindData |  |
| 293 | `__kmpc_process_loop_nest_rectang` | `0x628A0` | 38 | UnwindData |  |
| 153 | `__kmp_launch_worker` | `0x64A80` | 553 | UnwindData |  |
| 154 | `__kmp_reap_worker` | `0x64D70` | 31,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `__kmpc_omp_task_with_deps` | `0x6C800` | 121 | UnwindData |  |
| 292 | `__kmpc_omp_taskwait_deps_51` | `0x6C9E0` | 632 | UnwindData |  |
| 243 | `__kmpc_omp_wait_deps` | `0x6CC60` | 40 | UnwindData |  |
| 244 | `__kmpc_cancel` | `0x6CD10` | 177 | UnwindData |  |
| 246 | `__kmpc_cancel_barrier` | `0x6CDD0` | 209 | UnwindData |  |
| 245 | `__kmpc_cancellationpoint` | `0x6CEB0` | 166 | UnwindData |  |
| 1747 | `KMP_ALIGNED_MALLOC` | `0x6CF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1725 | `KMP_CALLOC` | `0x6CF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1853 | `KMP_CREATE_AFFINITY_MASK` | `0x6CF80` | 144 | UnwindData |  |
| 1854 | `KMP_DESTROY_AFFINITY_MASK` | `0x6D010` | 11 | UnwindData |  |
| 1726 | `KMP_FREE` | `0x6D130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1851 | `KMP_GET_AFFINITY` | `0x6D140` | 171 | UnwindData |  |
| 1859 | `KMP_GET_AFFINITY_MASK_PROC` | `0x6D1F0` | 118 | UnwindData |  |
| 1852 | `KMP_GET_AFFINITY_MAX_PROC` | `0x6D270` | 107 | UnwindData |  |
| 1727 | `KMP_GET_BLOCKTIME` | `0x6D2E0` | 168 | UnwindData |  |
| 1868 | `KMP_GET_CANCELLATION_STATUS` | `0x6D390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1728 | `KMP_GET_LIBRARY` | `0x6D3A0` | 30 | UnwindData |  |
| 1743 | `KMP_GET_NUM_KNOWN_THREADS` | `0x6D3C0` | 30 | UnwindData |  |
| 1729 | `KMP_GET_STACKSIZE` | `0x6D3E0` | 30 | UnwindData |  |
| 1745 | `KMP_GET_STACKSIZE_S` | `0x6D400` | 31 | UnwindData |  |
| 1730 | `KMP_MALLOC` | `0x6D420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1732 | `KMP_REALLOC` | `0x6D430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1850 | `KMP_SET_AFFINITY` | `0x6D440` | 123 | UnwindData |  |
| 1855 | `KMP_SET_AFFINITY_MASK_PROC` | `0x6D4C0` | 118 | UnwindData |  |
| 1734 | `KMP_SET_BLOCKTIME` | `0x6D540` | 94 | UnwindData |  |
| 1746 | `KMP_SET_DEFAULTS` | `0x6D660` | 83 | UnwindData |  |
| 1890 | `KMP_SET_DISP_NUM_BUFFERS` | `0x6D6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `KMP_SET_LIBRARY` | `0x6D6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `KMP_SET_LIBRARY_SERIAL` | `0x6D6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1738 | `KMP_SET_LIBRARY_THROUGHPUT` | `0x6D700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `KMP_SET_LIBRARY_TURNAROUND` | `0x6D710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1741 | `KMP_SET_STACKSIZE` | `0x6D720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1744 | `KMP_SET_STACKSIZE_S` | `0x6D730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1780 | `KMP_SET_WARNINGS_OFF` | `0x6D740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1779 | `KMP_SET_WARNINGS_ON` | `0x6D750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1857 | `KMP_UNSET_AFFINITY_MASK_PROC` | `0x6D760` | 118 | UnwindData |  |
| 1751 | `OMP_CAPTURE_AFFINITY` | `0x6D7E0` | 395 | UnwindData |  |
| 1891 | `OMP_CONTROL_TOOL` | `0x6D970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1898 | `OMP_DESTROY_ALLOCATOR` | `0x6D980` | 29 | UnwindData |  |
| 1700 | `OMP_DESTROY_LOCK` | `0x6D9A0` | 31 | UnwindData |  |
| 1701 | `OMP_DESTROY_NEST_LOCK` | `0x6D9C0` | 31 | UnwindData |  |
| 1750 | `OMP_DISPLAY_AFFINITY` | `0x6D9E0` | 213 | UnwindData |  |
| 1733 | `OMP_DISPLAY_ENV` | `0x6DAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1759 | `OMP_FULFILL_EVENT` | `0x6DAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1789 | `OMP_GET_ACTIVE_LEVEL` | `0x6DAE0` | 38 | UnwindData |  |
| 1749 | `OMP_GET_AFFINITY_FORMAT` | `0x6DB10` | 185 | UnwindData |  |
| 1791 | `OMP_GET_ANCESTOR_THREAD_NUM` | `0x6DBD0` | 27 | UnwindData |  |
| 1867 | `OMP_GET_CANCELLATION` | `0x6DBF0` | 30 | UnwindData |  |
| 1893 | `OMP_GET_DEFAULT_ALLOCATOR` | `0x6DC10` | 20 | UnwindData |  |
| 1880 | `OMP_GET_DEFAULT_DEVICE` | `0x6DC30` | 38 | UnwindData |  |
| 1815 | `OMP_GET_DEVICES_ALLOCATOR` | `0x6DC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `OMP_GET_DEVICES_ALL_ALLOCATOR` | `0x6DC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `OMP_GET_DEVICES_ALL_MEMSPACE` | `0x6DC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1817 | `OMP_GET_DEVICES_AND_HOST_ALLOCATOR` | `0x6DCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1812 | `OMP_GET_DEVICES_AND_HOST_MEMSPACE` | `0x6DCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `OMP_GET_DEVICES_MEMSPACE` | `0x6DCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `OMP_GET_DEVICE_ALLOCATOR` | `0x6DCE0` | 36 | UnwindData |  |
| 1818 | `OMP_GET_DEVICE_AND_HOST_ALLOCATOR` | `0x6DD10` | 37 | UnwindData |  |
| 1813 | `OMP_GET_DEVICE_AND_HOST_MEMSPACE` | `0x6DD40` | 37 | UnwindData |  |
| 1822 | `OMP_GET_DEVICE_FROM_UID` | `0x6DD70` | 110 | UnwindData |  |
| 1811 | `OMP_GET_DEVICE_MEMSPACE` | `0x6DDE0` | 36 | UnwindData |  |
| 1896 | `OMP_GET_DEVICE_NUM` | `0x6DE10` | 73 | UnwindData |  |
| 1702 | `OMP_GET_DYNAMIC` | `0x6DE60` | 43 | UnwindData |  |
| 1882 | `OMP_GET_INITIAL_DEVICE` | `0x6DE90` | 73 | UnwindData |  |
| 1807 | `OMP_GET_INTEROP_INT` | `0x6DEE0` | 84 | UnwindData |  |
| 1808 | `OMP_GET_INTEROP_PTR` | `0x6DF40` | 84 | UnwindData |  |
| 1809 | `OMP_GET_INTEROP_STR` | `0x6DFA0` | 84 | UnwindData |  |
| 1790 | `OMP_GET_LEVEL` | `0x6E000` | 38 | UnwindData |  |
| 1794 | `OMP_GET_MAX_ACTIVE_LEVELS` | `0x6E030` | 35 | UnwindData |  |
| 1872 | `OMP_GET_MAX_TASK_PRIORITY` | `0x6E060` | 30 | UnwindData |  |
| 1803 | `OMP_GET_MAX_TEAMS` | `0x6E080` | 28 | UnwindData |  |
| 1703 | `OMP_GET_MAX_THREADS` | `0x6E0A0` | 83 | UnwindData |  |
| 1820 | `OMP_GET_MEMSPACE_NUM_RESOURCES` | `0x6E100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1704 | `OMP_GET_NESTED` | `0x6E110` | 170 | UnwindData |  |
| 1881 | `OMP_GET_NUM_DEVICES` | `0x6E1C0` | 73 | UnwindData |  |
| 1873 | `OMP_GET_NUM_PLACES` | `0x6E210` | 93 | UnwindData |  |
| 1705 | `OMP_GET_NUM_PROCS` | `0x6E270` | 76 | UnwindData |  |
| 1865 | `OMP_GET_NUM_TEAMS` | `0x6E2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `OMP_GET_NUM_THREADS` | `0x6E2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1877 | `OMP_GET_PARTITION_NUM_PLACES` | `0x6E2E0` | 148 | UnwindData |  |
| 1878 | `OMP_GET_PARTITION_PLACE_NUMS` | `0x6E380` | 34 | UnwindData |  |
| 1876 | `OMP_GET_PLACE_NUM` | `0x6E420` | 29 | UnwindData |  |
| 1874 | `OMP_GET_PLACE_NUM_PROCS` | `0x6E4A0` | 120 | UnwindData |  |
| 1875 | `OMP_GET_PLACE_PROC_IDS` | `0x6E5B0` | 128 | UnwindData |  |
| 1862 | `OMP_GET_PROC_BIND` | `0x6E6C0` | 38 | UnwindData |  |
| 1796 | `OMP_GET_SCHEDULE` | `0x6E6F0` | 44 | UnwindData |  |
| 1821 | `OMP_GET_SUBMEMSPACE` | `0x6E720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `OMP_GET_SUPPORTED_ACTIVE_LEVELS` | `0x6E730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1805 | `OMP_GET_TEAMS_THREAD_LIMIT` | `0x6E740` | 28 | UnwindData |  |
| 1866 | `OMP_GET_TEAM_NUM` | `0x6E760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1792 | `OMP_GET_TEAM_SIZE` | `0x6E770` | 27 | UnwindData |  |
| 1793 | `OMP_GET_THREAD_LIMIT` | `0x6E790` | 67 | UnwindData |  |
| 1707 | `OMP_GET_THREAD_NUM` | `0x6E7E0` | 60 | UnwindData |  |
| 1823 | `OMP_GET_UID_FROM_DEVICE` | `0x6E820` | 50 | UnwindData |  |
| 1708 | `OMP_GET_WTICK` | `0x6E860` | 40 | UnwindData |  |
| 1709 | `OMP_GET_WTIME` | `0x6E890` | 40 | UnwindData |  |
| 1897 | `OMP_INIT_ALLOCATOR` | `0x6E8C0` | 59 | UnwindData |  |
| 1711 | `OMP_INIT_LOCK` | `0x6E900` | 31 | UnwindData |  |
| 1870 | `OMP_INIT_LOCK_WITH_HINT` | `0x6E920` | 46 | UnwindData |  |
| 1712 | `OMP_INIT_NEST_LOCK` | `0x6E950` | 31 | UnwindData |  |
| 1871 | `OMP_INIT_NEST_LOCK_WITH_HINT` | `0x6E970` | 46 | UnwindData |  |
| 1769 | `OMP_IN_EXPLICIT_TASK` | `0x6E9A0` | 42 | UnwindData |  |
| 1861 | `OMP_IN_FINAL` | `0x6E9D0` | 58 | UnwindData |  |
| 1710 | `OMP_IN_PARALLEL` | `0x6EA10` | 71 | UnwindData |  |
| 1869 | `OMP_IS_INITIAL_DEVICE` | `0x6EA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `OMP_PAUSE_RESOURCE` | `0x6EA70` | 159 | UnwindData |  |
| 1757 | `OMP_PAUSE_RESOURCE_ALL` | `0x6EB10` | 64 | UnwindData |  |
| 1748 | `OMP_SET_AFFINITY_FORMAT` | `0x6EB50` | 161 | UnwindData |  |
| 1892 | `OMP_SET_DEFAULT_ALLOCATOR` | `0x6EC00` | 29 | UnwindData |  |
| 1879 | `OMP_SET_DEFAULT_DEVICE` | `0x6EC20` | 43 | UnwindData |  |
| 1713 | `OMP_SET_DYNAMIC` | `0x6EC50` | 67 | UnwindData |  |
| 1714 | `OMP_SET_LOCK` | `0x6ECA0` | 31 | UnwindData |  |
| 1795 | `OMP_SET_MAX_ACTIVE_LEVELS` | `0x6ECC0` | 27 | UnwindData |  |
| 1716 | `OMP_SET_NESTED` | `0x6ECE0` | 206 | UnwindData |  |
| 1715 | `OMP_SET_NEST_LOCK` | `0x6EDB0` | 31 | UnwindData |  |
| 1802 | `OMP_SET_NUM_TEAMS` | `0x6EDD0` | 36 | UnwindData |  |
| 1717 | `OMP_SET_NUM_THREADS` | `0x6EE00` | 28 | UnwindData |  |
| 1797 | `OMP_SET_SCHEDULE` | `0x6EE20` | 41 | UnwindData |  |
| 1804 | `OMP_SET_TEAMS_THREAD_LIMIT` | `0x6EE50` | 36 | UnwindData |  |
| 1718 | `OMP_TEST_LOCK` | `0x6EE80` | 31 | UnwindData |  |
| 1719 | `OMP_TEST_NEST_LOCK` | `0x6EEA0` | 31 | UnwindData |  |
| 1720 | `OMP_UNSET_LOCK` | `0x6EEC0` | 31 | UnwindData |  |
| 1721 | `OMP_UNSET_NEST_LOCK` | `0x6EEE0` | 31 | UnwindData |  |
| 747 | `kmp_aligned_malloc` | `0x6F0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 725 | `kmp_calloc` | `0x6F0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 853 | `kmp_create_affinity_mask` | `0x6F0E0` | 144 | UnwindData |  |
| 854 | `kmp_destroy_affinity_mask` | `0x6F170` | 11 | UnwindData |  |
| 726 | `kmp_free` | `0x6F290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `kmp_get_affinity` | `0x6F2A0` | 171 | UnwindData |  |
| 859 | `kmp_get_affinity_mask_proc` | `0x6F350` | 114 | UnwindData |  |
| 852 | `kmp_get_affinity_max_proc` | `0x6F3D0` | 107 | UnwindData |  |
| 727 | `kmp_get_blocktime` | `0x6F440` | 168 | UnwindData |  |
| 868 | `kmp_get_cancellation_status` | `0x6F4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `kmp_get_library` | `0x6F500` | 30 | UnwindData |  |
| 743 | `kmp_get_num_known_threads` | `0x6F520` | 30 | UnwindData |  |
| 729 | `kmp_get_stacksize` | `0x6F540` | 30 | UnwindData |  |
| 745 | `kmp_get_stacksize_s` | `0x6F560` | 31 | UnwindData |  |
| 730 | `kmp_malloc` | `0x6F580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 732 | `kmp_realloc` | `0x6F590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `kmp_set_affinity` | `0x6F5A0` | 123 | UnwindData |  |
| 855 | `kmp_set_affinity_mask_proc` | `0x6F620` | 114 | UnwindData |  |
| 734 | `kmp_set_blocktime` | `0x6F6A0` | 92 | UnwindData |  |
| 746 | `kmp_set_defaults` | `0x6F7C0` | 55 | UnwindData |  |
| 890 | `kmp_set_disp_num_buffers` | `0x6F800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `kmp_set_library` | `0x6F820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `kmp_set_library_serial` | `0x6F830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `kmp_set_library_throughput` | `0x6F840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `kmp_set_library_turnaround` | `0x6F850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `kmp_set_stacksize` | `0x6F860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `kmp_set_stacksize_s` | `0x6F870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `kmp_set_warnings_off` | `0x6F880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `kmp_set_warnings_on` | `0x6F890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 857 | `kmp_unset_affinity_mask_proc` | `0x6F8A0` | 114 | UnwindData |  |
| 751 | `omp_capture_affinity` | `0x6F920` | 395 | UnwindData |  |
| 891 | `omp_control_tool` | `0x6FAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 898 | `omp_destroy_allocator` | `0x6FAC0` | 29 | UnwindData |  |
| 700 | `omp_destroy_lock` | `0x6FAE0` | 31 | UnwindData |  |
| 701 | `omp_destroy_nest_lock` | `0x6FB00` | 31 | UnwindData |  |
| 750 | `omp_display_affinity` | `0x6FB20` | 213 | UnwindData |  |
| 733 | `omp_display_env` | `0x6FC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 759 | `omp_fulfill_event` | `0x6FC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `omp_get_active_level` | `0x6FC20` | 38 | UnwindData |  |
| 749 | `omp_get_affinity_format` | `0x6FC50` | 185 | UnwindData |  |
| 791 | `omp_get_ancestor_thread_num` | `0x6FD10` | 27 | UnwindData |  |
| 867 | `omp_get_cancellation` | `0x6FD30` | 30 | UnwindData |  |
| 893 | `omp_get_default_allocator` | `0x6FD50` | 20 | UnwindData |  |
| 880 | `omp_get_default_device` | `0x6FD70` | 38 | UnwindData |  |
| 816 | `omp_get_device_allocator` | `0x6FDA0` | 34 | UnwindData |  |
| 818 | `omp_get_device_and_host_allocator` | `0x6FDD0` | 35 | UnwindData |  |
| 813 | `omp_get_device_and_host_memspace` | `0x6FE00` | 35 | UnwindData |  |
| 822 | `omp_get_device_from_uid` | `0x6FE30` | 110 | UnwindData |  |
| 811 | `omp_get_device_memspace` | `0x6FEA0` | 34 | UnwindData |  |
| 896 | `omp_get_device_num` | `0x6FED0` | 73 | UnwindData |  |
| 819 | `omp_get_devices_all_allocator` | `0x6FF20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `omp_get_devices_all_memspace` | `0x6FF40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `omp_get_devices_allocator` | `0x6FF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | `omp_get_devices_and_host_allocator` | `0x6FF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 812 | `omp_get_devices_and_host_memspace` | `0x6FF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 810 | `omp_get_devices_memspace` | `0x6FF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `omp_get_dynamic` | `0x6FFA0` | 43 | UnwindData |  |
| 882 | `omp_get_initial_device` | `0x6FFD0` | 73 | UnwindData |  |
| 807 | `omp_get_interop_int` | `0x70020` | 84 | UnwindData |  |
| 808 | `omp_get_interop_ptr` | `0x70080` | 84 | UnwindData |  |
| 809 | `omp_get_interop_str` | `0x700E0` | 84 | UnwindData |  |
| 790 | `omp_get_level` | `0x70140` | 38 | UnwindData |  |
| 794 | `omp_get_max_active_levels` | `0x70170` | 35 | UnwindData |  |
| 872 | `omp_get_max_task_priority` | `0x701A0` | 30 | UnwindData |  |
| 803 | `omp_get_max_teams` | `0x701C0` | 28 | UnwindData |  |
| 703 | `omp_get_max_threads` | `0x701E0` | 83 | UnwindData |  |
| 820 | `omp_get_memspace_num_resources` | `0x70240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `omp_get_nested` | `0x70250` | 170 | UnwindData |  |
| 881 | `omp_get_num_devices` | `0x70300` | 73 | UnwindData |  |
| 873 | `omp_get_num_places` | `0x70350` | 93 | UnwindData |  |
| 705 | `omp_get_num_procs` | `0x703B0` | 76 | UnwindData |  |
| 865 | `omp_get_num_teams` | `0x70400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `omp_get_num_threads` | `0x70410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `omp_get_partition_num_places` | `0x70420` | 148 | UnwindData |  |
| 878 | `omp_get_partition_place_nums` | `0x704C0` | 34 | UnwindData |  |
| 876 | `omp_get_place_num` | `0x70560` | 29 | UnwindData |  |
| 874 | `omp_get_place_num_procs` | `0x705E0` | 120 | UnwindData |  |
| 875 | `omp_get_place_proc_ids` | `0x706F0` | 128 | UnwindData |  |
| 862 | `omp_get_proc_bind` | `0x70800` | 38 | UnwindData |  |
| 796 | `omp_get_schedule` | `0x70830` | 44 | UnwindData |  |
| 821 | `omp_get_submemspace` | `0x70860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 758 | `omp_get_supported_active_levels` | `0x70870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `omp_get_team_num` | `0x70880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 792 | `omp_get_team_size` | `0x70890` | 27 | UnwindData |  |
| 805 | `omp_get_teams_thread_limit` | `0x708B0` | 28 | UnwindData |  |
| 793 | `omp_get_thread_limit` | `0x708D0` | 67 | UnwindData |  |
| 707 | `omp_get_thread_num` | `0x70920` | 60 | UnwindData |  |
| 823 | `omp_get_uid_from_device` | `0x70960` | 50 | UnwindData |  |
| 708 | `omp_get_wtick` | `0x709A0` | 40 | UnwindData |  |
| 709 | `omp_get_wtime` | `0x709D0` | 40 | UnwindData |  |
| 769 | `omp_in_explicit_task` | `0x70A00` | 42 | UnwindData |  |
| 861 | `omp_in_final` | `0x70A30` | 58 | UnwindData |  |
| 710 | `omp_in_parallel` | `0x70A70` | 71 | UnwindData |  |
| 897 | `omp_init_allocator` | `0x70AC0` | 59 | UnwindData |  |
| 711 | `omp_init_lock` | `0x70B00` | 31 | UnwindData |  |
| 870 | `omp_init_lock_with_hint` | `0x70B20` | 46 | UnwindData |  |
| 712 | `omp_init_nest_lock` | `0x70B50` | 31 | UnwindData |  |
| 871 | `omp_init_nest_lock_with_hint` | `0x70B70` | 46 | UnwindData |  |
| 869 | `omp_is_initial_device` | `0x70BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `omp_pause_resource` | `0x70BB0` | 159 | UnwindData |  |
| 757 | `omp_pause_resource_all` | `0x70C50` | 64 | UnwindData |  |
| 748 | `omp_set_affinity_format` | `0x70C90` | 161 | UnwindData |  |
| 892 | `omp_set_default_allocator` | `0x70D40` | 29 | UnwindData |  |
| 879 | `omp_set_default_device` | `0x70D60` | 43 | UnwindData |  |
| 713 | `omp_set_dynamic` | `0x70D90` | 65 | UnwindData |  |
| 714 | `omp_set_lock` | `0x70DE0` | 31 | UnwindData |  |
| 795 | `omp_set_max_active_levels` | `0x70E00` | 27 | UnwindData |  |
| 715 | `omp_set_nest_lock` | `0x70E20` | 31 | UnwindData |  |
| 716 | `omp_set_nested` | `0x70E40` | 204 | UnwindData |  |
| 802 | `omp_set_num_teams` | `0x70F10` | 35 | UnwindData |  |
| 717 | `omp_set_num_threads` | `0x70F40` | 27 | UnwindData |  |
| 797 | `omp_set_schedule` | `0x70F60` | 41 | UnwindData |  |
| 804 | `omp_set_teams_thread_limit` | `0x70F90` | 35 | UnwindData |  |
| 718 | `omp_test_lock` | `0x70FC0` | 31 | UnwindData |  |
| 719 | `omp_test_nest_lock` | `0x70FE0` | 31 | UnwindData |  |
| 720 | `omp_unset_lock` | `0x71000` | 31 | UnwindData |  |
| 721 | `omp_unset_nest_lock` | `0x71020` | 31 | UnwindData |  |
| 152 | `__kmp_invoke_microtask` | `0x713A0` | 153 | UnwindData |  |
| 236 | `omp_null_mem_space` | `0x739F8` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `omp_default_mem_space` | `0x73A00` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `omp_large_cap_mem_space` | `0x73A08` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `omp_const_mem_space` | `0x73A10` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `omp_high_bw_mem_space` | `0x73A18` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `omp_low_lat_mem_space` | `0x73A20` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `omp_cgroup_mem_space` | `0x73A28` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `llvm_omp_target_host_mem_space` | `0x73A30` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `llvm_omp_target_shared_mem_space` | `0x73A38` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `llvm_omp_target_device_mem_space` | `0x73A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `omp_null_allocator` | `0x73A50` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `omp_default_mem_alloc` | `0x73A58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `omp_large_cap_mem_alloc` | `0x73A60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `omp_const_mem_alloc` | `0x73A68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `omp_high_bw_mem_alloc` | `0x73A70` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `omp_low_lat_mem_alloc` | `0x73A78` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `omp_cgroup_mem_alloc` | `0x73A80` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `omp_pteam_mem_alloc` | `0x73A88` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `omp_thread_mem_alloc` | `0x73A90` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `llvm_omp_target_host_mem_alloc` | `0x73A98` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `llvm_omp_target_shared_mem_alloc` | `0x73AA0` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `llvm_omp_target_device_mem_alloc` | `0x73AA8` | 0 | Indeterminate |  |
