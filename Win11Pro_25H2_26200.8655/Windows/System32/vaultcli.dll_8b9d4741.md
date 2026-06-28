# Binary Specification: vaultcli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\vaultcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8b9d4741af77ac96518fd2f3fc8e6df05ba4839774bf51f45dda4fcaed9a986d`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 109 | `DllGetActivationFactory` | `0x10580` | 875 | UnwindData |  |
| 108 | `DllCanUnloadNow` | `0x14BF0` | 352 | UnwindData |  |
| 107 | *Ordinal Only* | `0x16640` | 532 | UnwindData |  |
| 124 | `VaultRemoveItem` | `0x16860` | 178 | UnwindData |  |
| 121 | `VaultGetItem` | `0x16920` | 288 | UnwindData |  |
| 123 | `VaultOpenVault` | `0x16A50` | 172 | UnwindData |  |
| 122 | `VaultGetItemType` | `0x16B10` | 251 | UnwindData |  |
| 112 | `VaultCloseVault` | `0x16C20` | 140 | UnwindData |  |
| 110 | `DllGetClassObject` | `0x18230` | 116 | UnwindData |  |
| 119 | `VaultFree` | `0x18960` | 86 | UnwindData |  |
| 118 | `VaultFindItems` | `0x1AA80` | 243 | UnwindData |  |
| 116 | `VaultEnumerateItems` | `0x1C600` | 225 | UnwindData |  |
| 106 | *Ordinal Only* | `0x1EA40` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0x1EDF0` | 144 | UnwindData |  |
| 101 | *Ordinal Only* | `0x1EE90` | 160 | UnwindData |  |
| 102 | *Ordinal Only* | `0x1EF40` | 223 | UnwindData |  |
| 104 | *Ordinal Only* | `0x1F030` | 144 | UnwindData |  |
| 105 | *Ordinal Only* | `0x1F0D0` | 122 | UnwindData |  |
| 111 | `VaultAddItem` | `0x1F270` | 185 | UnwindData |  |
| 113 | `VaultCreateItemType` | `0x1F330` | 282 | UnwindData |  |
| 114 | `VaultDeleteItemType` | `0x1F450` | 231 | UnwindData |  |
| 115 | `VaultEnumerateItemTypes` | `0x1F540` | 321 | UnwindData |  |
| 117 | `VaultEnumerateVaults` | `0x1F690` | 206 | UnwindData |  |
| 120 | `VaultGetInformation` | `0x1F770` | 143 | UnwindData |  |
