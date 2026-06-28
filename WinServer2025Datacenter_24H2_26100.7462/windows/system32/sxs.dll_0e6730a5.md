# Binary Specification: sxs.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sxs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0e6730a54e9c928de73ce1701b4daa14f55f527e805a51bd1ae11bedd289231e`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 16 | `SxsOleAut32MapIIDToTLBPath` | `0x7D60` | 37 | UnwindData |  |
| 15 | `SxsOleAut32MapIIDToProxyStubCLSID` | `0x2E010` | 43 | UnwindData |  |
| 8 | `CreateAssemblyNameObject` | `0x30A30` | 479 | UnwindData |  |
| 17 | `SxsOleAut32MapReferenceClsidToConfiguredClsid` | `0x31A70` | 331 | UnwindData |  |
| 18 | `SxsOleAut32RedirectTypeLibrary` | `0x31FC0` | 385 | UnwindData |  |
| 19 | `SxsProbeAssemblyInstallation` | `0x34020` | 1,282 | UnwindData |  |
| 13 | `SxsOleAut32MapConfiguredClsidToReferenceClsid` | `0x4AA00` | 452 | UnwindData |  |
| 3 | `SxsLookupClrGuid` | `0x4FF70` | 1,596 | UnwindData |  |
| 1 | `SxsFindClrClassInformation` | `0x505C0` | 1,506 | UnwindData |  |
| 2 | `SxsFindClrSurrogateInformation` | `0x50BB0` | 1,104 | UnwindData |  |
| 7 | `CreateAssemblyCache` | `0x59590` | 378 | UnwindData |  |
| 11 | `SxsGenerateActivationContext` | `0x5AA40` | 2,249 | UnwindData |  |
| 14 | `SxsOleAut32MapIIDOrCLSIDToTypeLibrary` | `0x5DA60` | 397 | UnwindData |  |
| 21 | `SxsUninstallW` | `0x5DC00` | 777 | UnwindData |  |
| 4 | `SxsRunDllInstallAssembly` | `0x5DFF0` | 238 | UnwindData |  |
| 5 | `SxsRunDllInstallAssemblyW` | `0x5E0F0` | 309 | UnwindData |  |
| 9 | `SxsBeginAssemblyInstall` | `0x5E410` | 631 | UnwindData |  |
| 10 | `SxsEndAssemblyInstall` | `0x5E690` | 496 | UnwindData |  |
| 12 | `SxsInstallW` | `0x5E890` | 1,653 | UnwindData |  |
| 6 | `SxspGenerateManifestPathOnAssemblyIdentity` | `0x5FCC0` | 547 | UnwindData |  |
| 20 | `SxsQueryManifestInformation` | `0x624B0` | 370 | UnwindData |  |
