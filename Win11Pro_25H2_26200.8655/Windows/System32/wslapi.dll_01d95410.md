# Binary Specification: wslapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wslapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `01d9541014988bb41371e639e2367adaa78529ffab38d341f1d3516d060c74ce`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x6B40` | 32 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x6B70` | 65 | UnwindData |  |
| 3 | `DllMain` | `0x6BC0` | 174 | UnwindData |  |
| 4 | `WslConfigureDistribution` | `0x7210` | 157 | UnwindData |  |
| 5 | `WslGetDistributionConfiguration` | `0x72C0` | 176 | UnwindData |  |
| 6 | `WslIsDistributionRegistered` | `0x7CA0` | 127 | UnwindData |  |
| 9 | `WslRegisterDistribution` | `0x7D30` | 143 | UnwindData |  |
| 10 | `WslUnregisterDistribution` | `0x7DD0` | 130 | UnwindData |  |
| 7 | `WslLaunch` | `0x84B0` | 191 | UnwindData |  |
| 8 | `WslLaunchInteractive` | `0x8580` | 160 | UnwindData |  |
