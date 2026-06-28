# Binary Specification: WinHvPlatform.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WinHvPlatform.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b4384abf61ee98349fc4b0e967d4049ad95d409b9adde5343b6553d9097c062e`
* **Total Exported Functions:** 66

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `WHvGetInterruptTargetVpSet` | `0xB350` | 341 | UnwindData |  |
| 23 | `WHvGetVirtualProcessorCpuidOutput` | `0xB4B0` | 339 | UnwindData |  |
| 24 | `WHvGetVirtualProcessorInterruptControllerState` | `0xB610` | 186 | UnwindData |  |
| 25 | `WHvGetVirtualProcessorInterruptControllerState2` | `0xB6D0` | 186 | UnwindData |  |
| 28 | `WHvGetVirtualProcessorXsaveState` | `0xB790` | 261 | UnwindData |  |
| 41 | `WHvRequestInterrupt` | `0xB8A0` | 243 | UnwindData |  |
| 49 | `WHvSetVirtualProcessorInterruptControllerState` | `0xB9A0` | 138 | UnwindData |  |
| 50 | `WHvSetVirtualProcessorInterruptControllerState2` | `0xBA30` | 138 | UnwindData |  |
| 53 | `WHvSetVirtualProcessorXsaveState` | `0xBAC0` | 225 | UnwindData |  |
| 3 | `WHvAllocateVpciResource` | `0x2C780` | 1,335 | UnwindData |  |
| 12 | `WHvCreateVpciDevice` | `0x2CCC0` | 257 | UnwindData |  |
| 17 | `WHvDeleteVpciDevice` | `0x2CDD0` | 279 | UnwindData |  |
| 29 | `WHvGetVpciDeviceInterruptTarget` | `0x2CEF0` | 163 | UnwindData |  |
| 30 | `WHvGetVpciDeviceNotification` | `0x2CFA0` | 382 | UnwindData |  |
| 31 | `WHvGetVpciDeviceProperty` | `0x2D130` | 475 | UnwindData |  |
| 34 | `WHvMapVpciDeviceInterrupt` | `0x2D320` | 125 | UnwindData |  |
| 35 | `WHvMapVpciDeviceMmioRanges` | `0x2D3B0` | 90 | UnwindData |  |
| 39 | `WHvReadVpciDeviceRegister` | `0x2D410` | 136 | UnwindData |  |
| 42 | `WHvRequestVpciDeviceInterrupt` | `0x2D4A0` | 175 | UnwindData |  |
| 45 | `WHvRetargetVpciDeviceInterrupt` | `0x2D560` | 631 | UnwindData |  |
| 54 | `WHvSetVpciDevicePowerState` | `0x2D7E0` | 326 | UnwindData |  |
| 61 | `WHvUnmapVpciDeviceInterrupt` | `0x2D930` | 318 | UnwindData |  |
| 62 | `WHvUnmapVpciDeviceMmioRanges` | `0x2DA80` | 64 | UnwindData |  |
| 66 | `WHvWriteVpciDeviceRegister` | `0x2DAD0` | 136 | UnwindData |  |
| 1 | `WHvAcceptPartitionMigration` | `0x2E2F0` | 169 | UnwindData |  |
| 2 | `WHvAdviseGpaRange` | `0x2E3A0` | 241 | UnwindData |  |
| 4 | `WHvCancelPartitionMigration` | `0x2E4A0` | 108 | UnwindData |  |
| 5 | `WHvCancelRunVirtualProcessor` | `0x2E520` | 136 | UnwindData |  |
| 6 | `WHvCompletePartitionMigration` | `0x2E5B0` | 108 | UnwindData |  |
| 7 | `WHvCreateNotificationPort` | `0x2E630` | 164 | UnwindData |  |
| 8 | `WHvCreatePartition` | `0x2E6E0` | 136 | UnwindData |  |
| 9 | `WHvCreateTrigger` | `0x2E770` | 242 | UnwindData |  |
| 10 | `WHvCreateVirtualProcessor` | `0x2E870` | 127 | UnwindData |  |
| 11 | `WHvCreateVirtualProcessor2` | `0x2E900` | 216 | UnwindData |  |
| 13 | `WHvDeleteNotificationPort` | `0x2E9E0` | 122 | UnwindData |  |
| 14 | `WHvDeletePartition` | `0x2EA60` | 143 | UnwindData |  |
| 15 | `WHvDeleteTrigger` | `0x2EB00` | 122 | UnwindData |  |
| 16 | `WHvDeleteVirtualProcessor` | `0x2EB80` | 80 | UnwindData |  |
| 18 | `WHvGetCapability` | `0x2EBE0` | 1,969 | UnwindData |  |
| 20 | `WHvGetPartitionCounters` | `0x2F3A0` | 190 | UnwindData |  |
| 21 | `WHvGetPartitionProperty` | `0x2F470` | 178 | UnwindData |  |
| 22 | `WHvGetVirtualProcessorCounters` | `0x2F530` | 294 | UnwindData |  |
| 26 | `WHvGetVirtualProcessorRegisters` | `0x2F660` | 335 | UnwindData |  |
| 27 | `WHvGetVirtualProcessorState` | `0x2F7C0` | 253 | UnwindData |  |
| 32 | `WHvMapGpaRange` | `0x2F8D0` | 162 | UnwindData |  |
| 33 | `WHvMapGpaRange2` | `0x2F980` | 162 | UnwindData |  |
| 36 | `WHvPostVirtualProcessorSynicMessage` | `0x2FA30` | 333 | UnwindData |  |
| 37 | `WHvQueryGpaRangeDirtyBitmap` | `0x2FB90` | 142 | UnwindData |  |
| 38 | `WHvReadGpaRange` | `0x2FC30` | 243 | UnwindData |  |
| 40 | `WHvRegisterPartitionDoorbellEvent` | `0x2FD30` | 102 | UnwindData |  |
| 43 | `WHvResetPartition` | `0x2FDA0` | 68 | UnwindData |  |
| 44 | `WHvResumePartitionTime` | `0x2FDF0` | 68 | UnwindData |  |
| 46 | `WHvRunVirtualProcessor` | `0x2FE40` | 126 | UnwindData |  |
| 47 | `WHvSetNotificationPortProperty` | `0x2FED0` | 162 | UnwindData |  |
| 48 | `WHvSetPartitionProperty` | `0x2FF80` | 123 | UnwindData |  |
| 51 | `WHvSetVirtualProcessorRegisters` | `0x30010` | 335 | UnwindData |  |
| 52 | `WHvSetVirtualProcessorState` | `0x30170` | 169 | UnwindData |  |
| 55 | `WHvSetupPartition` | `0x30220` | 85 | UnwindData |  |
| 56 | `WHvSignalVirtualProcessorSynicEvent` | `0x30280` | 268 | UnwindData |  |
| 57 | `WHvStartPartitionMigration` | `0x303A0` | 122 | UnwindData |  |
| 58 | `WHvSuspendPartitionTime` | `0x30420` | 155 | UnwindData |  |
| 59 | `WHvTranslateGva` | `0x304D0` | 257 | UnwindData |  |
| 60 | `WHvUnmapGpaRange` | `0x305E0` | 163 | UnwindData |  |
| 63 | `WHvUnregisterPartitionDoorbellEvent` | `0x30690` | 83 | UnwindData |  |
| 64 | `WHvUpdateTriggerParameters` | `0x306F0` | 231 | UnwindData |  |
| 65 | `WHvWriteGpaRange` | `0x307E0` | 243 | UnwindData |  |
