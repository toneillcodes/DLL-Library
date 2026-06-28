# Binary Specification: netprovfw.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netprovfw.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c74cbc4b72a8d83af76b170e2dd71f180ab70037a383815fdd2082eb29777133`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `NetpProvDomainJoinLicensingCheck` | `0x0` | - | Forwarded | Forwarded to: `JOINUTIL.NetpDoDomainJoinLicensingCheck` |
| 6 | `NetpProvCheckOfflineLsaPolicyUpdate` | `0x1D10` | 1,299 | UnwindData |  |
| 9 | `NetpProvFreeLdapLsaDomainInfo` | `0x2230` | 134 | UnwindData |  |
| 2 | `NetCreateProvisioningPackage` | `0x22C0` | 948 | UnwindData |  |
| 5 | `NetpCreateProvisioningPackage` | `0x2790` | 854 | UnwindData |  |
| 3 | `NetRequestProvisioningPackageInstall` | `0x37E0` | 104 | UnwindData |  |
| 4 | `NetpAnalyzeProvisioningPackage` | `0x3EA0` | 165 | UnwindData |  |
| 10 | `NetpRequestProvisioningPackageInstall` | `0x4D60` | 37 | UnwindData |  |
| 11 | `NetpRequestProvisioningPackageInstallForIMC` | `0x4D90` | 289 | UnwindData |  |
| 12 | `NetpRequestProvisioningPackageInstallForOfflineServicing` | `0x4EC0` | 197 | UnwindData |  |
| 7 | `NetpProvContinueProvisioningPackageInstall` | `0x5F70` | 618 | UnwindData |  |
| 1 | `NetCaptureProvisioningPackage` | `0x63E0` | 209 | UnwindData |  |
