# Binary Specification: wdsutil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\oobe\wdsutil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eea3785724985f0e7a8bb4698edb3d1d53ac445143b23e690dae374737f0f0f6`
* **Total Exported Functions:** 323

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 315 | `IsCrossArchitectureInstall` | `0x2640` | 254 | UnwindData |  |
| 318 | `SignalSetupComplianceBlock` | `0x2750` | 368 | UnwindData |  |
| 224 | `DiskRegionSupportsCapabilityForType` | `0x2AB0` | 400 | UnwindData |  |
| 225 | `DiskSupportsCapabilityForType` | `0x2C50` | 320 | UnwindData |  |
| 226 | `FreeReason` | `0x2DA0` | 164 | UnwindData |  |
| 227 | `GetApplicableDiskReason` | `0x2E50` | 444 | UnwindData |  |
| 228 | `GetApplicableDiskRegionReason` | `0x3020` | 521 | UnwindData |  |
| 230 | `GetDiskKey` | `0x34E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `GetRegionKey` | `0x3510` | 158 | UnwindData |  |
| 235 | `LogDiskReasons` | `0x35C0` | 64 | UnwindData |  |
| 236 | `LogDiskRegionReasons` | `0x38E0` | 85 | UnwindData |  |
| 1 | `??0?$CShimUserSetting@VCStringUserSetting@@@@QEAA@AEBV0@@Z` | `0x3F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0?$CShimUserSetting@VCUInt32UserSetting@@@@QEAA@AEBV0@@Z` | `0x3F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0?$CShimUserSetting@VCUInt64UserSetting@@@@QEAA@AEBV0@@Z` | `0x3F00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$CShimUserSetting@VCStringUserSetting@@@@QEAA@XZ` | `0x3F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0?$CShimUserSetting@VCUInt32UserSetting@@@@QEAA@XZ` | `0x3F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0?$CShimUserSetting@VCUInt64UserSetting@@@@QEAA@XZ` | `0x3F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0CComputerNameSetting@@QEAA@$$QEAV0@@Z` | `0x3F60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CComputerNameSetting@@QEAA@AEBV0@@Z` | `0x3F60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0CComputerNameSetting@@QEAA@XZ` | `0x3FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0CDUUIProgressSetting@@QEAA@$$QEAV0@@Z` | `0x3FC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0CDUUIProgressSetting@@QEAA@AEBV0@@Z` | `0x3FC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??0CDUUIProgressSetting@@QEAA@XZ` | `0x4000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0CDUUIWelcomeSetting@@QEAA@$$QEAV0@@Z` | `0x4020` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??0CDUUIWelcomeSetting@@QEAA@AEBV0@@Z` | `0x4020` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0CDUUIWelcomeSetting@@QEAA@XZ` | `0x4060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `??0CDiskPartFileSystemUserSetting@@QEAA@$$QEAV0@@Z` | `0x4080` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0CDiskPartFileSystemUserSetting@@QEAA@AEBV0@@Z` | `0x4080` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `??0CDiskPartFileSystemUserSetting@@QEAA@XZ` | `0x40C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `??0CDiskPartFormatUserSetting@@QEAA@$$QEAV0@@Z` | `0x40E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `??0CDiskPartFormatUserSetting@@QEAA@AEBV0@@Z` | `0x40E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0CDiskPartFormatUserSetting@@QEAA@XZ` | `0x4120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??0CDiskPartUserSetting@@QEAA@$$QEAV0@@Z` | `0x4140` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??0CDiskPartUserSetting@@QEAA@AEBV0@@Z` | `0x4140` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??0CDiskPartUserSetting@@QEAA@XZ` | `0x4180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??0CEulaSetting@@QEAA@$$QEAV0@@Z` | `0x41A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0CEulaSetting@@QEAA@AEBV0@@Z` | `0x41A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0CEulaSetting@@QEAA@XZ` | `0x41E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0CIBSUIImageSelectionSetting@@QEAA@$$QEAV0@@Z` | `0x4200` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??0CIBSUIImageSelectionSetting@@QEAA@AEBV0@@Z` | `0x4200` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??0CIBSUIImageSelectionSetting@@QEAA@XZ` | `0x4240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??0CKeyboardSetting@@QEAA@$$QEAV0@@Z` | `0x4260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0CKeyboardSetting@@QEAA@AEBV0@@Z` | `0x4260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??0CKeyboardSetting@@QEAA@XZ` | `0x42A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `??0COOBEUIFinishSetting@@QEAA@$$QEAV0@@Z` | `0x42C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??0COOBEUIFinishSetting@@QEAA@AEBV0@@Z` | `0x42C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??0COOBEUIFinishSetting@@QEAA@XZ` | `0x4300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0COOBEUIWelcomeSetting@@QEAA@$$QEAV0@@Z` | `0x4320` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??0COOBEUIWelcomeSetting@@QEAA@AEBV0@@Z` | `0x4320` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??0COOBEUIWelcomeSetting@@QEAA@XZ` | `0x4360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??0CProductKeyUserSetting@@QEAA@$$QEAV0@@Z` | `0x4380` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??0CProductKeyUserSetting@@QEAA@AEBV0@@Z` | `0x4380` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0CProductKeyUserSetting@@QEAA@XZ` | `0x43C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??0CSetupUISummarySetting@@QEAA@$$QEAV0@@Z` | `0x43E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `??0CSetupUISummarySetting@@QEAA@AEBV0@@Z` | `0x43E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??0CSetupUISummarySetting@@QEAA@XZ` | `0x4420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??0CSetupUIWelcomeSetting@@QEAA@$$QEAV0@@Z` | `0x4440` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??0CSetupUIWelcomeSetting@@QEAA@AEBV0@@Z` | `0x4440` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??0CSetupUIWelcomeSetting@@QEAA@XZ` | `0x4480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0CShimStringUserSetting@@QEAA@$$QEAV0@@Z` | `0x44A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `??0CShimStringUserSetting@@QEAA@AEBV0@@Z` | `0x44A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??0CShimStringUserSetting@@QEAA@XZ` | `0x44E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0CShimUInt32UserSetting@@QEAA@$$QEAV0@@Z` | `0x4500` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??0CShimUInt32UserSetting@@QEAA@AEBV0@@Z` | `0x4500` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0CShimUInt32UserSetting@@QEAA@XZ` | `0x4540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??0CShimUInt64UserSetting@@QEAA@$$QEAV0@@Z` | `0x4560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0CShimUInt64UserSetting@@QEAA@AEBV0@@Z` | `0x4560` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??0CShimUInt64UserSetting@@QEAA@XZ` | `0x45A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0CShowFlagUserSetting@@IEAA@XZ` | `0x45C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??0CShowFlagUserSetting@@QEAA@AEBV0@@Z` | `0x45E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??0CSimpleStringUserSetting@@QEAA@$$QEAV0@@Z` | `0x4620` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??0CSimpleStringUserSetting@@QEAA@AEBV0@@Z` | `0x4620` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??0CSimpleStringUserSetting@@QEAA@XZ` | `0x4660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `??0CSimpleUInt32UserSetting@@QEAA@$$QEAV0@@Z` | `0x4680` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??0CSimpleUInt32UserSetting@@QEAA@AEBV0@@Z` | `0x4680` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??0CSimpleUInt32UserSetting@@QEAA@XZ` | `0x46C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??0CSimpleUInt64UserSetting@@QEAA@$$QEAV0@@Z` | `0x46E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??0CSimpleUInt64UserSetting@@QEAA@AEBV0@@Z` | `0x46E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??0CSimpleUInt64UserSetting@@QEAA@XZ` | `0x4720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??0CStringUserSetting@@IEAA@XZ` | `0x4740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0CUInt32UserSetting@@IEAA@XZ` | `0x4740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??0CUInt64UserSetting@@IEAA@XZ` | `0x4740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `??0CStringUserSetting@@QEAA@AEBV0@@Z` | `0x4760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??0CUInt32UserSetting@@QEAA@AEBV0@@Z` | `0x4760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `??0CUInt64UserSetting@@QEAA@AEBV0@@Z` | `0x4760` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??0CTimezoneSetting@@QEAA@$$QEAV0@@Z` | `0x47A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0CTimezoneSetting@@QEAA@AEBV0@@Z` | `0x47A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??0CTimezoneSetting@@QEAA@XZ` | `0x47E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `??0CUpgStoreUserSetting@@QEAA@$$QEAV0@@Z` | `0x4800` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `??0CUpgStoreUserSetting@@QEAA@AEBV0@@Z` | `0x4800` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `??0CUpgStoreUserSetting@@QEAA@XZ` | `0x4840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `??0CUpgradeUserSetting@@QEAA@$$QEAV0@@Z` | `0x4860` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??0CUpgradeUserSetting@@QEAA@AEBV0@@Z` | `0x4860` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `??0CUpgradeUserSetting@@QEAA@XZ` | `0x48A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??0CUserSetting@@QEAA@AEBV0@@Z` | `0x48C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `??0CUserSetting@@QEAA@XZ` | `0x48F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??0CWDSUIImageSelectionSetting@@QEAA@$$QEAV0@@Z` | `0x4910` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??0CWDSUIImageSelectionSetting@@QEAA@AEBV0@@Z` | `0x4910` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `??0CWDSUIImageSelectionSetting@@QEAA@XZ` | `0x4950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `??0CWDSUIWelcomeSetting@@QEAA@$$QEAV0@@Z` | `0x4970` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `??0CWDSUIWelcomeSetting@@QEAA@AEBV0@@Z` | `0x4970` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??0CWDSUIWelcomeSetting@@QEAA@XZ` | `0x49B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `??1?$CShimUserSetting@VCStringUserSetting@@@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??1?$CShimUserSetting@VCUInt32UserSetting@@@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??1?$CShimUserSetting@VCUInt64UserSetting@@@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `??1CComputerNameSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `??1CDiskPartFileSystemUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `??1CDiskPartFormatUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `??1CDiskPartUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `??1CEulaSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `??1CKeyboardSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `??1CProductKeyUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `??1CShimStringUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `??1CShimUInt32UserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `??1CShimUInt64UserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `??1CSimpleStringUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `??1CSimpleUInt32UserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `??1CSimpleUInt64UserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `??1CStringUserSetting@@IEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `??1CTimezoneSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??1CUInt32UserSetting@@IEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `??1CUInt64UserSetting@@IEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `??1CUpgStoreUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `??1CUpgradeUserSetting@@QEAA@XZ` | `0x49D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `??1CDUUIProgressSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `??1CDUUIWelcomeSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `??1CIBSUIImageSelectionSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `??1COOBEUIFinishSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `??1COOBEUIWelcomeSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `??1CSetupUISummarySetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `??1CSetupUIWelcomeSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `??1CShowFlagUserSetting@@IEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `??1CWDSUIImageSelectionSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??1CWDSUIWelcomeSetting@@QEAA@XZ` | `0x49F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `??1CUserSetting@@QEAA@XZ` | `0x4A10` | 78 | UnwindData |  |
| 125 | `??4?$CShimUserSetting@VCStringUserSetting@@@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `??4?$CShimUserSetting@VCStringUserSetting@@@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `??4?$CShimUserSetting@VCUInt32UserSetting@@@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??4?$CShimUserSetting@VCUInt32UserSetting@@@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `??4?$CShimUserSetting@VCUInt64UserSetting@@@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `??4?$CShimUserSetting@VCUInt64UserSetting@@@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `??4CComputerNameSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `??4CComputerNameSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `??4CDUUIProgressSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `??4CDUUIProgressSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `??4CDUUIWelcomeSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??4CDUUIWelcomeSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `??4CDiskPartFileSystemUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??4CDiskPartFileSystemUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `??4CDiskPartFormatUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `??4CDiskPartFormatUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `??4CDiskPartUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `??4CDiskPartUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??4CEulaSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `??4CEulaSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `??4CIBSUIImageSelectionSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `??4CIBSUIImageSelectionSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `??4CKeyboardSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `??4CKeyboardSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `??4COOBEUIFinishSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `??4COOBEUIFinishSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `??4COOBEUIWelcomeSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `??4COOBEUIWelcomeSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `??4CProductKeyUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `??4CProductKeyUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `??4CSetupUISummarySetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `??4CSetupUISummarySetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `??4CSetupUIWelcomeSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `??4CSetupUIWelcomeSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `??4CShimStringUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `??4CShimStringUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `??4CShimUInt32UserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `??4CShimUInt32UserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `??4CShimUInt64UserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `??4CShimUInt64UserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `??4CShowFlagUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `??4CSimpleStringUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `??4CSimpleStringUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `??4CSimpleUInt32UserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `??4CSimpleUInt32UserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `??4CSimpleUInt64UserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `??4CSimpleUInt64UserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `??4CStringUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `??4CTimezoneSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `??4CTimezoneSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `??4CUInt32UserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `??4CUInt64UserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `??4CUpgStoreUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `??4CUpgStoreUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `??4CUpgradeUserSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `??4CUpgradeUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `??4CUserSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `??4CWDSUIImageSelectionSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `??4CWDSUIImageSelectionSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `??4CWDSUIWelcomeSetting@@QEAAAEAV0@$$QEAV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `??4CWDSUIWelcomeSetting@@QEAAAEAV0@AEBV0@@Z` | `0x4A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?AcquireMutex@CUserSetting@@IEAAXXZ` | `0x4AA0` | 179 | UnwindData |  |
| 220 | `?DeserializeField@CUserSetting@@IEAAJPEBGIPEAUWDS_DATA@@H@Z` | `0x4B60` | 295 | UnwindData |  |
| 221 | `?DeserializeString@CStringUserSetting@@IEAAJPEAPEAGH@Z` | `0x4C90` | 363 | UnwindData |  |
| 222 | `?DeserializeUInt32@CUInt32UserSetting@@IEAAJPEAIH@Z` | `0x4E10` | 65 | UnwindData |  |
| 223 | `?DeserializeUInt64@CUInt64UserSetting@@IEAAJPEA_KH@Z` | `0x4E60` | 68 | UnwindData |  |
| 229 | `?GetBlackboard@CUserSetting@@IEAAPEAU_BLACKBOARD@@XZ` | `0x4EB0` | 122 | UnwindData |  |
| 231 | `?GetKeyName@CUserSetting@@IEAAJPEAGHH@Z` | `0x4F30` | 142 | UnwindData |  |
| 232 | `?GetModuleId@CUserSetting@@QEAAPEAXXZ` | `0x4FD0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `?IsUpgrade@CUpgradeUserSetting@@SAHXZ` | `0x5030` | 130 | UnwindData |  |
| 237 | `?ReadError@CUserSetting@@IEAAJPEAJH@Z` | `0x50C0` | 130 | UnwindData |  |
| 238 | `?ReadShow@CUserSetting@@IEAAJPEAHH@Z` | `0x5150` | 65 | UnwindData |  |
| 239 | `?ReleaseMutex@CUserSetting@@IEAAXXZ` | `0x51A0` | 139 | UnwindData |  |
| 240 | `?SerializeField@CUserSetting@@IEAAXPEBGPEAUWDS_DATA@@@Z` | `0x5240` | 168 | UnwindData |  |
| 241 | `?SerializeString@CStringUserSetting@@IEAAXPEBG@Z` | `0x52F0` | 129 | UnwindData |  |
| 242 | `?SerializeUInt32@CUInt32UserSetting@@IEAAXI@Z` | `0x5380` | 61 | UnwindData |  |
| 243 | `?SerializeUInt64@CUInt64UserSetting@@IEAAX_K@Z` | `0x53D0` | 61 | UnwindData |  |
| 244 | `?SetModuleId@CUserSetting@@QEAAXPEAX@Z` | `0x5420` | 84 | UnwindData |  |
| 245 | `?Simple_get_String@CStringUserSetting@@IEAAJPEAPEAG@Z` | `0x5480` | 140 | UnwindData |  |
| 246 | `?Simple_get_UInt32@CUInt32UserSetting@@IEAAJPEAI@Z` | `0x5520` | 140 | UnwindData |  |
| 247 | `?Simple_get_UInt64@CUInt64UserSetting@@IEAAJPEA_K@Z` | `0x55C0` | 140 | UnwindData |  |
| 248 | `?Simple_set_String@CStringUserSetting@@IEAAJPEBG@Z` | `0x5660` | 17 | UnwindData |  |
| 305 | `?set_String@CSimpleStringUserSetting@@UEAAJPEBG@Z` | `0x5660` | 17 | UnwindData |  |
| 249 | `?Simple_set_UInt32@CUInt32UserSetting@@IEAAJI@Z` | `0x5680` | 17 | UnwindData |  |
| 308 | `?set_UInt32@CSimpleUInt32UserSetting@@UEAAJI@Z` | `0x5680` | 17 | UnwindData |  |
| 250 | `?Simple_set_UInt64@CUInt64UserSetting@@IEAAJ_K@Z` | `0x56A0` | 17 | UnwindData |  |
| 311 | `?set_UInt64@CSimpleUInt64UserSetting@@UEAAJ_K@Z` | `0x56A0` | 17 | UnwindData |  |
| 251 | `?UnattendChecked@CUpgradeUserSetting@@SAHXZ` | `0x5730` | 742 | UnwindData |  |
| 256 | `?get_Error@?$CShimUserSetting@VCStringUserSetting@@@@UEAAJPEAJ@Z` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?get_Error@?$CShimUserSetting@VCUInt32UserSetting@@@@UEAAJPEAJ@Z` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `?get_Error@?$CShimUserSetting@VCUInt64UserSetting@@@@UEAAJPEAJ@Z` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `?get_Error@CSimpleStringUserSetting@@UEAAJPEAJ@Z` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `?get_Error@CSimpleUInt32UserSetting@@UEAAJPEAJ@Z` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `?get_Error@CSimpleUInt64UserSetting@@UEAAJPEAJ@Z` | `0x5A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?get_Error@CShowFlagUserSetting@@UEAAJPEAJ@Z` | `0x5A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?get_Name@CComputerNameSetting@@EEAAPEAGXZ` | `0x5A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `?get_Name@CDUUIProgressSetting@@EEAAPEAGXZ` | `0x5A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `?get_Name@CDUUIWelcomeSetting@@EEAAPEAGXZ` | `0x5A60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `?get_Name@CDiskPartFileSystemUserSetting@@EEAAPEAGXZ` | `0x5A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `?get_Name@CDiskPartFormatUserSetting@@EEAAPEAGXZ` | `0x5A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `?get_Name@CDiskPartUserSetting@@EEAAPEAGXZ` | `0x5AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `?get_Name@CEulaSetting@@EEAAPEAGXZ` | `0x5AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `?get_Name@CIBSUIImageSelectionSetting@@EEAAPEAGXZ` | `0x5AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `?get_Name@CKeyboardSetting@@EEAAPEAGXZ` | `0x5AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `?get_Name@COOBEUIFinishSetting@@EEAAPEAGXZ` | `0x5AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `?get_Name@COOBEUIWelcomeSetting@@EEAAPEAGXZ` | `0x5AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `?get_Name@CProductKeyUserSetting@@EEAAPEAGXZ` | `0x5B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 275 | `?get_Name@CSetupUISummarySetting@@EEAAPEAGXZ` | `0x5B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `?get_Name@CSetupUIWelcomeSetting@@EEAAPEAGXZ` | `0x5B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `?get_Name@CTimezoneSetting@@EEAAPEAGXZ` | `0x5B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 278 | `?get_Name@CUpgStoreUserSetting@@EEAAPEAGXZ` | `0x5B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `?get_Name@CUpgradeUserSetting@@EEAAPEAGXZ` | `0x5B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `?get_Name@CWDSUIImageSelectionSetting@@EEAAPEAGXZ` | `0x5B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 281 | `?get_Name@CWDSUIWelcomeSetting@@EEAAPEAGXZ` | `0x5B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 282 | `?get_Show@?$CShimUserSetting@VCStringUserSetting@@@@UEAAJPEAH@Z` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `?get_Show@?$CShimUserSetting@VCUInt32UserSetting@@@@UEAAJPEAH@Z` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `?get_Show@?$CShimUserSetting@VCUInt64UserSetting@@@@UEAAJPEAH@Z` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 288 | `?get_Show@CSimpleStringUserSetting@@UEAAJPEAH@Z` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `?get_Show@CSimpleUInt32UserSetting@@UEAAJPEAH@Z` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 290 | `?get_Show@CSimpleUInt64UserSetting@@UEAAJPEAH@Z` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 285 | `?get_Show@CComputerNameSetting@@UEAAJPEAH@Z` | `0x5BA0` | 86 | UnwindData |  |
| 286 | `?get_Show@CDiskPartUserSetting@@UEAAJPEAH@Z` | `0x5C00` | 105 | UnwindData |  |
| 287 | `?get_Show@CShowFlagUserSetting@@UEAAJPEAH@Z` | `0x5C70` | 130 | UnwindData |  |
| 291 | `?get_String@CShimStringUserSetting@@UEAAJPEAPEAG@Z` | `0x5D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `?get_String@CSimpleStringUserSetting@@UEAAJPEAPEAG@Z` | `0x5D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `?get_UInt32@CDiskPartUserSetting@@UEAAJPEAI@Z` | `0x5D10` | 857 | UnwindData |  |
| 294 | `?get_UInt32@CShimUInt32UserSetting@@UEAAJPEAI@Z` | `0x6070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `?get_UInt32@CSimpleUInt32UserSetting@@UEAAJPEAI@Z` | `0x6070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `?get_UInt64@CShimUInt64UserSetting@@UEAAJPEA_K@Z` | `0x6080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `?get_UInt64@CSimpleUInt64UserSetting@@UEAAJPEA_K@Z` | `0x6080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `?get_ValidateID@CComputerNameSetting@@EEAAHXZ` | `0x6090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 299 | `?get_ValidateID@CDiskPartUserSetting@@EEAAHXZ` | `0x60A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `?get_ValidateID@CProductKeyUserSetting@@EEAAHXZ` | `0x60B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `?set_Error@CUserSetting@@QEAAJJ@Z` | `0x60C0` | 63 | UnwindData |  |
| 302 | `?set_Show@CUserSetting@@QEAAJH@Z` | `0x6110` | 63 | UnwindData |  |
| 303 | `?set_String@CComputerNameSetting@@UEAAJPEBG@Z` | `0x6160` | 24 | UnwindData |  |
| 304 | `?set_String@CShimStringUserSetting@@UEAAJPEBG@Z` | `0x6180` | 239 | UnwindData |  |
| 306 | `?set_UInt32@CDiskPartUserSetting@@UEAAJI@Z` | `0x6280` | 2,455 | UnwindData |  |
| 307 | `?set_UInt32@CShimUInt32UserSetting@@UEAAJI@Z` | `0x6C20` | 237 | UnwindData |  |
| 309 | `?set_UInt32@CUpgradeUserSetting@@UEAAJI@Z` | `0x6D20` | 234 | UnwindData |  |
| 310 | `?set_UInt64@CShimUInt64UserSetting@@UEAAJ_K@Z` | `0x6E10` | 239 | UnwindData |  |
| 312 | `CallbackGetArgumentInt32` | `0x70C0` | 33 | UnwindData |  |
| 313 | `CallbackGetArgumentString` | `0x70F0` | 405 | UnwindData |  |
| 314 | `CallbackGetArgumentUInt64` | `0x7290` | 35 | UnwindData |  |
| 317 | `PublishMessage` | `0x72C0` | 1,100 | UnwindData |  |
| 319 | `WdsCollectionAddString` | `0x7720` | 136 | UnwindData |  |
| 320 | `WdsCollectionAddUInt32` | `0x77B0` | 131 | UnwindData |  |
| 321 | `WdsCollectionAddUInt64` | `0x7840` | 131 | UnwindData |  |
| 322 | `WdsPickTempDriveBasedOnInstallDrive` | `0x78D0` | 476 | UnwindData |  |
| 323 | `WdsValidateInstallDrive` | `0x7AC0` | 476 | UnwindData |  |
| 316 | `MergeEtlFiles` | `0x7F80` | 287 | UnwindData |  |
| 214 | `??_7CUpgStoreUserSetting@@6B@` | `0x36B28` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `??_7CDUUIProgressSetting@@6B@` | `0x36B50` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `??_7CTimezoneSetting@@6B@` | `0x36B68` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `??_7?$CShimUserSetting@VCStringUserSetting@@@@6B@` | `0x36B90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `??_7?$CShimUserSetting@VCUInt32UserSetting@@@@6B@` | `0x36B90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `??_7?$CShimUserSetting@VCUInt64UserSetting@@@@6B@` | `0x36B90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `??_7CProductKeyUserSetting@@6B@` | `0x36BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `??_7CComputerNameSetting@@6B@` | `0x36BF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `??_7COOBEUIWelcomeSetting@@6B@` | `0x36C20` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `??_7CStringUserSetting@@6B@` | `0x36C38` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `??_7CUInt32UserSetting@@6B@` | `0x36C38` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `??_7CUInt64UserSetting@@6B@` | `0x36C38` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `??_7COOBEUIFinishSetting@@6B@` | `0x36C60` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `??_7CWDSUIWelcomeSetting@@6B@` | `0x36C78` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `??_7CDUUIWelcomeSetting@@6B@` | `0x36C90` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `??_7CWDSUIImageSelectionSetting@@6B@` | `0x36CA8` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `??_7CIBSUIImageSelectionSetting@@6B@` | `0x36CE8` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `??_7CSetupUIWelcomeSetting@@6B@` | `0x36D00` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `??_7CSimpleUInt32UserSetting@@6B@` | `0x36D18` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `??_7CShowFlagUserSetting@@6B@` | `0x36D40` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `??_7CSimpleStringUserSetting@@6B@` | `0x36D58` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `??_7CKeyboardSetting@@6B@` | `0x36D80` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `??_7CDiskPartFormatUserSetting@@6B@` | `0x36DA8` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `??_7CDiskPartUserSetting@@6B@` | `0x36DD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `??_7CEulaSetting@@6B@` | `0x36E00` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `??_7CShimStringUserSetting@@6B@` | `0x36E28` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `??_7CUpgradeUserSetting@@6B@` | `0x36E58` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `??_7CShimUInt64UserSetting@@6B@` | `0x36E80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `??_7CShimUInt32UserSetting@@6B@` | `0x36EB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `??_7CSimpleUInt64UserSetting@@6B@` | `0x36EE0` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `??_7CUserSetting@@6B@` | `0x36F08` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 201 | `??_7CSetupUISummarySetting@@6B@` | `0x36F20` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `??_7CDiskPartFileSystemUserSetting@@6B@` | `0x36F38` | 3,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 254 | `?c_stShowName@CUserSetting@@1QEBGEB` | `0x37C58` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `?c_stValueName@CUserSetting@@1QEBGEB` | `0x37C60` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?c_stErrorName@CUserSetting@@1QEBGEB` | `0x37C68` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `?c_stMutex@CUserSetting@@1QEBGEB` | `0x37C70` | 0 | Indeterminate |  |
