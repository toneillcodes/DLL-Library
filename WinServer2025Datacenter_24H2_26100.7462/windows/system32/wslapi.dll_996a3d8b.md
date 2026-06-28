# Binary Specification: wslapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wslapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `996a3d8b908a6dec6105963e7c6a01d9802232bb600586f1bf991279d27c7e2e`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x6B20` | 32 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x6B50` | 65 | UnwindData |  |
| 3 | `DllMain` | `0x6BA0` | 174 | UnwindData |  |
| 4 | `WslConfigureDistribution` | `0x71F0` | 157 | UnwindData |  |
| 5 | `WslGetDistributionConfiguration` | `0x72A0` | 176 | UnwindData |  |
| 6 | `WslIsDistributionRegistered` | `0x7C80` | 127 | UnwindData |  |
| 9 | `WslRegisterDistribution` | `0x7D10` | 143 | UnwindData |  |
| 10 | `WslUnregisterDistribution` | `0x7DB0` | 130 | UnwindData |  |
| 7 | `WslLaunch` | `0x8490` | 191 | UnwindData |  |
| 8 | `WslLaunchInteractive` | `0x8560` | 160 | UnwindData |  |
