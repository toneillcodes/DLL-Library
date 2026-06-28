# Binary Specification: wldp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wldp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a28e7b387e6aa1bb3e5485b65421cdb0415d988c550ed5ab9ea94b532125fb9b`
* **Total Exported Functions:** 54

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | *Ordinal Only* | `0xAD00` | 1,248 | UnwindData |  |
| 50 | *Ordinal Only* | `0xB1F0` | 48,050 | UnwindData |  |
| 8 | `WldpQueryWindowsLockdownMode` | `0x18D00` | 153 | UnwindData |  |
| 4 | `WldpGetLockdownPolicy` | `0x18DA0` | 956 | UnwindData |  |
| 51 | *Ordinal Only* | `0x19240` | 420 | UnwindData |  |
| 20 | `WldpQueryPolicySettingEnabled2` | `0x1A000` | 31 | UnwindData |  |
| 18 | `WldpIsAppApprovedByPolicy` | `0x1DBB0` | 109 | UnwindData |  |
| 25 | `WldpIsAllowedEntryPoint` | `0x1E1C0` | 1,019 | UnwindData |  |
| 23 | `WldpIsProductionConfiguration` | `0x1F5F0` | 35 | UnwindData |  |
| 6 | `WldpIsDynamicCodePolicyEnabled` | `0x20CF0` | 122 | UnwindData |  |
| 15 | `WldpQueryWindowsLockdownRestriction` | `0x210F0` | 121 | UnwindData |  |
| 33 | *Ordinal Only* | `0x21650` | 4,848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WldpCanExecuteFile` | `0x22940` | 1,513 | UnwindData |  |
| 31 | *Ordinal Only* | `0x27DB0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | *Ordinal Only* | `0x28190` | 177 | UnwindData |  |
| 47 | *Ordinal Only* | `0x28250` | 241 | UnwindData |  |
| 14 | `WldpQueryDeviceSecurityInformation` | `0x28350` | 511 | UnwindData |  |
| 19 | `WldpQueryPolicySettingEnabled` | `0x2D210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WldpSetWindowsLockdownRestriction` | `0x2D240` | 301 | UnwindData |  |
| 26 | `WldpAddDeveloperCertificateForDynamicCodeTrust` | `0x2D3D0` | 915 | UnwindData |  |
| 37 | *Ordinal Only* | `0x2D770` | 197 | UnwindData |  |
| 36 | *Ordinal Only* | `0x2D840` | 612 | UnwindData |  |
| 5 | `WldpIsClassInApprovedList` | `0x2DAB0` | 1,789 | UnwindData |  |
| 17 | `WldpIsDebugAllowed` | `0x2E1C0` | 461 | UnwindData |  |
| 7 | `WldpQueryDynamicCodeTrust` | `0x2E3F0` | 108 | UnwindData |  |
| 32 | `WldpQuerySecurityPolicy` | `0x2E470` | 98 | UnwindData |  |
| 9 | `WldpSetDynamicCodeTrust` | `0x2E4E0` | 67 | UnwindData |  |
| 34 | *Ordinal Only* | `0x2E530` | 2,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | *Ordinal Only* | `0x2ED60` | 458 | UnwindData |  |
| 46 | *Ordinal Only* | `0x2F310` | 182 | UnwindData |  |
| 42 | *Ordinal Only* | `0x2F620` | 566 | UnwindData |  |
| 43 | *Ordinal Only* | `0x2FB40` | 63 | UnwindData |  |
| 44 | *Ordinal Only* | `0x2FB90` | 262 | UnwindData |  |
| 45 | *Ordinal Only* | `0x2FE10` | 369 | UnwindData |  |
| 21 | `WldpIsWcosProductionConfiguration` | `0x30220` | 1,064 | UnwindData |  |
| 24 | `WldpResetProductionConfiguration` | `0x30650` | 240 | UnwindData |  |
| 22 | `WldpResetWcosProductionConfiguration` | `0x30750` | 99 | UnwindData |  |
| 48 | *Ordinal Only* | `0x30820` | 354 | UnwindData |  |
| 27 | `WldpCheckDeviceEncryptionNotStarted` | `0x30AE0` | 203 | UnwindData |  |
| 28 | `WldpCheckWcosDeviceEncryptionSecure` | `0x30BC0` | 283 | UnwindData |  |
| 41 | *Ordinal Only* | `0x364D0` | 151 | UnwindData |  |
| 40 | *Ordinal Only* | `0x36570` | 128 | UnwindData |  |
| 39 | *Ordinal Only* | `0x36600` | 149 | UnwindData |  |
| 1 | `WldpCanExecuteBuffer` | `0x36CD0` | 748 | UnwindData |  |
| 13 | `WldpCanExecuteFileFromDetachedSignature` | `0x36FD0` | 1,697 | UnwindData |  |
| 3 | `WldpCanExecuteStream` | `0x37680` | 719 | UnwindData |  |
| 29 | `WldpSendSmartAppControlBlockToast2` | `0x39620` | 84 | UnwindData |  |
| 30 | `WldpSendSmartAppControlSwitchEnforceToast` | `0x396E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `WldpSendWhqlOnlyBlockToast` | `0x396F0` | 20 | UnwindData |  |
| 10 | `WldpGetApplicationSettingBoolean` | `0x3D490` | 805 | UnwindData |  |
| 11 | `WldpGetApplicationSettingStringList` | `0x3D7C0` | 775 | UnwindData |  |
| 12 | `WldpGetApplicationSettingStringSet` | `0x3DAD0` | 775 | UnwindData |  |
| 52 | `WldpInstallEndpointSecurityPolicy` | `0x3EC30` | 421 | UnwindData |  |
| 53 | `WldpUninstallEndpointSecurityPolicy` | `0x3EDE0` | 355 | UnwindData |  |
