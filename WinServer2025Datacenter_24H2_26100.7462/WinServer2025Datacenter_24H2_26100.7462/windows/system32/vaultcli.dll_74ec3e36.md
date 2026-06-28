# Binary Specification: vaultcli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\vaultcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `74ec3e360cac60584af6a704539a76a20be2e8978f97007070ec9b64777179e4`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 109 | `DllGetActivationFactory` | `0x10550` | 875 | UnwindData |  |
| 108 | `DllCanUnloadNow` | `0x14BC0` | 352 | UnwindData |  |
| 107 | *Ordinal Only* | `0x16610` | 532 | UnwindData |  |
| 124 | `VaultRemoveItem` | `0x16830` | 178 | UnwindData |  |
| 121 | `VaultGetItem` | `0x168F0` | 288 | UnwindData |  |
| 123 | `VaultOpenVault` | `0x16A20` | 172 | UnwindData |  |
| 122 | `VaultGetItemType` | `0x16AE0` | 251 | UnwindData |  |
| 112 | `VaultCloseVault` | `0x16BF0` | 140 | UnwindData |  |
| 110 | `DllGetClassObject` | `0x18200` | 116 | UnwindData |  |
| 119 | `VaultFree` | `0x189D0` | 86 | UnwindData |  |
| 118 | `VaultFindItems` | `0x1AAE0` | 243 | UnwindData |  |
| 116 | `VaultEnumerateItems` | `0x1C5B0` | 225 | UnwindData |  |
| 106 | *Ordinal Only* | `0x1E9F0` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | *Ordinal Only* | `0x1EDA0` | 144 | UnwindData |  |
| 101 | *Ordinal Only* | `0x1EE40` | 160 | UnwindData |  |
| 102 | *Ordinal Only* | `0x1EEF0` | 223 | UnwindData |  |
| 104 | *Ordinal Only* | `0x1EFE0` | 144 | UnwindData |  |
| 105 | *Ordinal Only* | `0x1F080` | 122 | UnwindData |  |
| 111 | `VaultAddItem` | `0x1F220` | 185 | UnwindData |  |
| 113 | `VaultCreateItemType` | `0x1F2E0` | 282 | UnwindData |  |
| 114 | `VaultDeleteItemType` | `0x1F400` | 231 | UnwindData |  |
| 115 | `VaultEnumerateItemTypes` | `0x1F4F0` | 321 | UnwindData |  |
| 117 | `VaultEnumerateVaults` | `0x1F640` | 206 | UnwindData |  |
| 120 | `VaultGetInformation` | `0x1F720` | 143 | UnwindData |  |
