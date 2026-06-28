# Binary Specification: nvoglv64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\nvoglv64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5b723e66f1c2254d58804beab0de83d09447e08c5728f4050489a5301a9827d8`
* **Total Exported Functions:** 32

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 26 | `vkGetProcAddressNV` | `0x97F730` | 71 | UnwindData |  |
| 1 | `DrvCopyContext` | `0x987E90` | 472 | UnwindData |  |
| 2 | `DrvCreateContext` | `0x988160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DrvCreateLayerContext` | `0x988170` | 53 | UnwindData |  |
| 4 | `DrvDeleteContext` | `0x9881B0` | 325 | UnwindData |  |
| 5 | `DrvDescribeLayerPlane` | `0x9888E0` | 71 | UnwindData |  |
| 6 | `DrvDescribePixelFormat` | `0x988B60` | 72 | UnwindData |  |
| 7 | `DrvGetLayerPaletteEntries` | `0x989090` | 867 | UnwindData |  |
| 8 | `DrvGetProcAddress` | `0x989400` | 54 | UnwindData |  |
| 10 | `DrvRealizeLayerPalette` | `0x989590` | 778 | UnwindData |  |
| 11 | `DrvReleaseContext` | `0x9898A0` | 357 | UnwindData |  |
| 12 | `DrvSetCallbackProcs` | `0x989A10` | 54 | UnwindData |  |
| 13 | `DrvSetContext` | `0x989C60` | 1,926 | UnwindData |  |
| 14 | `DrvSetLayerPaletteEntries` | `0x98A3F0` | 1,098 | UnwindData |  |
| 15 | `DrvSetPixelFormat` | `0x98A840` | 585 | UnwindData |  |
| 16 | `DrvShareLists` | `0x98AA90` | 383 | UnwindData |  |
| 17 | `DrvSwapBuffers` | `0x98ADD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `DrvSwapLayerBuffers` | `0x98ADE0` | 756 | UnwindData |  |
| 19 | `DrvValidateVersion` | `0x98B0E0` | 58 | UnwindData |  |
| 20 | `DllMain` | `0x99BF90` | 835 | UnwindData |  |
| 9 | `DrvPresentBuffers` | `0x9BF130` | 2,761 | UnwindData |  |
| 31 | `vk_optimusGetDeviceProcAddr` | `0xD31B70` | 80 | UnwindData |  |
| 32 | `vk_optimusGetInstanceProcAddr` | `0xD31BC0` | 303 | UnwindData |  |
| 21 | `vkCreateInstance` | `0xD79880` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `vkEnumerateInstanceExtensionProperties` | `0xD7A050` | 34 | UnwindData |  |
| 23 | `vkEnumerateInstanceLayerProperties` | `0xD7A080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `vkEnumerateInstanceVersion` | `0xD7A090` | 1,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `vkGetInstanceProcAddr` | `0xD7A840` | 48 | UnwindData |  |
| 27 | `vk_icdEnumerateAdapterPhysicalDevices` | `0xE9E0A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `vk_icdGetInstanceProcAddr` | `0xE9E0C0` | 192 | UnwindData |  |
| 29 | `vk_icdGetPhysicalDeviceProcAddr` | `0xE9E180` | 132 | UnwindData |  |
| 30 | `vk_icdNegotiateLoaderICDInterfaceVersion` | `0xE9E210` | 5,842,069 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
