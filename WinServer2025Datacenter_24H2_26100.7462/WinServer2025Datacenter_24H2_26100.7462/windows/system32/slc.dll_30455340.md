# Binary Specification: slc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\slc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `304553401b7f872e11ca02c666cb09dfa978f12fe42f98c4e340b6c81931f54b`
* **Total Exported Functions:** 40

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `SLClose` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLClose` |
| 5 | `SLConsumeRight` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLConsumeRight` |
| 7 | `SLDepositOfflineConfirmationId` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLDepositOfflineConfirmationId` |
| 8 | `SLDepositOfflineConfirmationIdEx` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLDepositOfflineConfirmationIdEx` |
| 9 | `SLFireEvent` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLFireEvent` |
| 10 | `SLGenerateOfflineInstallationId` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGenerateOfflineInstallationId` |
| 11 | `SLGenerateOfflineInstallationIdEx` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGenerateOfflineInstallationIdEx` |
| 12 | `SLGetApplicationInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetApplicationInformation` |
| 13 | `SLGetGenuineInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetGenuineInformation` |
| 14 | `SLGetInstalledProductKeyIds` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetInstalledProductKeyIds` |
| 15 | `SLGetLicense` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetLicense` |
| 16 | `SLGetLicenseFileId` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetLicenseFileId` |
| 17 | `SLGetLicenseInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetLicenseInformation` |
| 18 | `SLGetLicensingStatusInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetLicensingStatusInformation` |
| 19 | `SLGetPKeyId` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetPKeyId` |
| 20 | `SLGetPKeyInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetPKeyInformation` |
| 21 | `SLGetPolicyInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetPolicyInformation` |
| 22 | `SLGetPolicyInformationDWORD` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetPolicyInformationDWORD` |
| 23 | `SLGetProductSkuInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetProductSkuInformation` |
| 24 | `SLGetSLIDList` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetSLIDList` |
| 25 | `SLGetServiceInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLGetServiceInformation` |
| 28 | `SLInstallLicense` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLInstallLicense` |
| 29 | `SLInstallProofOfPurchase` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLInstallProofOfPurchase` |
| 31 | `SLOpen` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLOpen` |
| 33 | `SLRegisterEvent` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLRegisterEvent` |
| 35 | `SLSetCurrentProductKey` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLSetCurrentProductKey` |
| 36 | `SLSetGenuineInformation` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLSetGenuineInformation` |
| 37 | `SLUninstallLicense` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLUninstallLicense` |
| 38 | `SLUninstallProofOfPurchase` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLUninstallProofOfPurchase` |
| 39 | `SLUnregisterEvent` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLUnregisterEvent` |
| 2 | `SLpGetGenuineLocal` | `0x0` | - | Forwarded | Forwarded to: `SPPC.SLpGetGenuineLocal` |
| 27 | `SLGetWindowsInformationDWORD` | `0x1140` | 66 | UnwindData |  |
| 26 | `SLGetWindowsInformation` | `0x7340` | 49,201 | UnwindData |  |
| 1 | `SLpCheckProductKey` | `0x1C540` | 59 | UnwindData |  |
| 3 | `SLpUpdateComponentTokens` | `0x1C590` | 326 | UnwindData |  |
| 6 | `SLConsumeWindowsRight` | `0x1D270` | 363 | UnwindData |  |
| 32 | `SLReArmWindows` | `0x1D3F0` | 119 | UnwindData |  |
| 34 | `SLRegisterWindowsEvent` | `0x1D470` | 81 | UnwindData |  |
| 40 | `SLUnregisterWindowsEvent` | `0x1D4D0` | 81 | UnwindData |  |
| 30 | `SLIsWindowsGenuineLocal` | `0x1D560` | 25,478 | UnwindData |  |
