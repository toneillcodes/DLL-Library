# Binary Specification: loadperf.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\loadperf.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ed4fdb7aae984b31e743415ce51d27d4ac02d6736990f2942903fdc946eb5860`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `InstallPerfDllA` | `0x7300` | 99 | UnwindData |  |
| 3 | `InstallPerfDllW` | `0x7370` | 403 | UnwindData |  |
| 4 | `LoadPerfCounterTextStringsA` | `0x7510` | 95 | UnwindData |  |
| 5 | `LoadPerfCounterTextStringsW` | `0x7580` | 388 | UnwindData |  |
| 9 | `SetServiceAsTrustedA` | `0x7910` | 102 | UnwindData |  |
| 10 | `SetServiceAsTrustedW` | `0x7980` | 764 | UnwindData |  |
| 13 | `UpdatePerfNameFilesA` | `0x7C90` | 213 | UnwindData |  |
| 14 | `UpdatePerfNameFilesW` | `0x7D70` | 178 | UnwindData |  |
| 11 | `UnloadPerfCounterTextStringsA` | `0x9160` | 95 | UnwindData |  |
| 12 | `UnloadPerfCounterTextStringsW` | `0x91D0` | 450 | UnwindData |  |
| 1 | `BackupPerfRegistryToFileW` | `0xB260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RestorePerfRegistryFromFileW` | `0xB280` | 1,891 | UnwindData |  |
| 6 | `LpAcquireInstallationMutex` | `0xB9F0` | 136 | UnwindData |  |
| 7 | `LpReleaseInstallationMutex` | `0xBA80` | 85 | UnwindData |  |
