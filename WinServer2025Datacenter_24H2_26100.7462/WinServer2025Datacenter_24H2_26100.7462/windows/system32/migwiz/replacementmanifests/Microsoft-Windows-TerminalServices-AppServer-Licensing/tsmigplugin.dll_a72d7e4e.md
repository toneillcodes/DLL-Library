# Binary Specification: tsmigplugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migwiz\replacementmanifests\Microsoft-Windows-TerminalServices-AppServer-Licensing\tsmigplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a72d7e4ea422606ccbe6e2ed8444e02a2d8fe83de04305c54b809c0c18b6b3e8`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x6130` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x6160` | 327 | UnwindData |  |
| 3 | `DllMain` | `0x62B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x62D0` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6400` | 151 | UnwindData |  |
