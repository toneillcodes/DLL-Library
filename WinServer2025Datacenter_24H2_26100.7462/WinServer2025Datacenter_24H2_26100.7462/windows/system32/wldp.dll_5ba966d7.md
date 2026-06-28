# Binary Specification: wldp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wldp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5ba966d79c231277ec2a93c547c558b918e6a8cf4f5a4cf1bcda5741b9e3a1cd`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | *Ordinal Only* | `0xB080` | 1,248 | UnwindData |  |
| 50 | *Ordinal Only* | `0xB570` | 48,050 | UnwindData |  |
| 8 | `WldpQueryWindowsLockdownMode` | `0x19080` | 153 | UnwindData |  |
| 4 | `WldpGetLockdownPolicy` | `0x19120` | 956 | UnwindData |  |
| 51 | *Ordinal Only* | `0x195C0` | 420 | UnwindData |  |
| 20 | `WldpQueryPolicySettingEnabled2` | `0x1A2D0` | 31 | UnwindData |  |
| 18 | `WldpIsAppApprovedByPolicy` | `0x1E490` | 109 | UnwindData |  |
| 25 | `WldpIsAllowedEntryPoint` | `0x1EB60` | 1,019 | UnwindData |  |
| 23 | `WldpIsProductionConfiguration` | `0x1FAE0` | 35 | UnwindData |  |
| 6 | `WldpIsDynamicCodePolicyEnabled` | `0x21400` | 122 | UnwindData |  |
| 15 | `WldpQueryWindowsLockdownRestriction` | `0x218D0` | 121 | UnwindData |  |
| 33 | *Ordinal Only* | `0x21E30` | 2,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WldpCanExecuteFile` | `0x22620` | 1,419 | UnwindData |  |
| 31 | *Ordinal Only* | `0x27610` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | *Ordinal Only* | `0x279F0` | 177 | UnwindData |  |
| 47 | *Ordinal Only* | `0x27AB0` | 241 | UnwindData |  |
| 14 | `WldpQueryDeviceSecurityInformation` | `0x27BB0` | 511 | UnwindData |  |
| 19 | `WldpQueryPolicySettingEnabled` | `0x2D610` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `WldpSetWindowsLockdownRestriction` | `0x2D640` | 301 | UnwindData |  |
| 26 | `WldpAddDeveloperCertificateForDynamicCodeTrust` | `0x2D7D0` | 915 | UnwindData |  |
| 37 | *Ordinal Only* | `0x2DB70` | 197 | UnwindData |  |
| 36 | *Ordinal Only* | `0x2DC40` | 612 | UnwindData |  |
| 5 | `WldpIsClassInApprovedList` | `0x2DEB0` | 1,789 | UnwindData |  |
| 17 | `WldpIsDebugAllowed` | `0x2E5C0` | 461 | UnwindData |  |
| 7 | `WldpQueryDynamicCodeTrust` | `0x2E7F0` | 108 | UnwindData |  |
| 32 | `WldpQuerySecurityPolicy` | `0x2E870` | 98 | UnwindData |  |
| 9 | `WldpSetDynamicCodeTrust` | `0x2E8E0` | 67 | UnwindData |  |
| 34 | *Ordinal Only* | `0x2E930` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | *Ordinal Only* | `0x2F130` | 458 | UnwindData |  |
| 46 | *Ordinal Only* | `0x2F6E0` | 182 | UnwindData |  |
| 42 | *Ordinal Only* | `0x2F9F0` | 566 | UnwindData |  |
| 43 | *Ordinal Only* | `0x2FF10` | 63 | UnwindData |  |
| 44 | *Ordinal Only* | `0x2FF60` | 262 | UnwindData |  |
| 45 | *Ordinal Only* | `0x301E0` | 369 | UnwindData |  |
| 21 | `WldpIsWcosProductionConfiguration` | `0x305F0` | 1,064 | UnwindData |  |
| 24 | `WldpResetProductionConfiguration` | `0x30A20` | 240 | UnwindData |  |
| 22 | `WldpResetWcosProductionConfiguration` | `0x30B20` | 99 | UnwindData |  |
| 48 | *Ordinal Only* | `0x30BF0` | 354 | UnwindData |  |
| 27 | `WldpCheckDeviceEncryptionNotStarted` | `0x30EB0` | 203 | UnwindData |  |
| 28 | `WldpCheckWcosDeviceEncryptionSecure` | `0x30F90` | 283 | UnwindData |  |
| 41 | *Ordinal Only* | `0x36370` | 151 | UnwindData |  |
| 40 | *Ordinal Only* | `0x36410` | 128 | UnwindData |  |
| 39 | *Ordinal Only* | `0x364A0` | 149 | UnwindData |  |
| 1 | `WldpCanExecuteBuffer` | `0x36B70` | 748 | UnwindData |  |
| 13 | `WldpCanExecuteFileFromDetachedSignature` | `0x36E70` | 1,687 | UnwindData |  |
| 3 | `WldpCanExecuteStream` | `0x37510` | 719 | UnwindData |  |
| 29 | `WldpSendSmartAppControlBlockToast2` | `0x38EC0` | 84 | UnwindData |  |
| 30 | `WldpSendSmartAppControlSwitchEnforceToast` | `0x38F80` | 15,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WldpGetApplicationSettingBoolean` | `0x3CCD0` | 805 | UnwindData |  |
| 11 | `WldpGetApplicationSettingStringList` | `0x3D000` | 775 | UnwindData |  |
| 12 | `WldpGetApplicationSettingStringSet` | `0x3D310` | 775 | UnwindData |  |
