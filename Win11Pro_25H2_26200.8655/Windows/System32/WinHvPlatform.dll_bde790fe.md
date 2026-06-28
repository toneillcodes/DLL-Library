# Binary Specification: WinHvPlatform.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WinHvPlatform.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bde790fec4292df7eecffa28a68211dfd0170f272f94a8d90415e6602111131c`
* **Total Exported Functions:** 66

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `WHvGetInterruptTargetVpSet` | `0xB370` | 341 | UnwindData |  |
| 23 | `WHvGetVirtualProcessorCpuidOutput` | `0xB4D0` | 339 | UnwindData |  |
| 24 | `WHvGetVirtualProcessorInterruptControllerState` | `0xB630` | 186 | UnwindData |  |
| 25 | `WHvGetVirtualProcessorInterruptControllerState2` | `0xB6F0` | 186 | UnwindData |  |
| 28 | `WHvGetVirtualProcessorXsaveState` | `0xB7B0` | 261 | UnwindData |  |
| 41 | `WHvRequestInterrupt` | `0xB8C0` | 243 | UnwindData |  |
| 49 | `WHvSetVirtualProcessorInterruptControllerState` | `0xB9C0` | 138 | UnwindData |  |
| 50 | `WHvSetVirtualProcessorInterruptControllerState2` | `0xBA50` | 138 | UnwindData |  |
| 53 | `WHvSetVirtualProcessorXsaveState` | `0xBAE0` | 225 | UnwindData |  |
| 3 | `WHvAllocateVpciResource` | `0x2C8D0` | 1,335 | UnwindData |  |
| 12 | `WHvCreateVpciDevice` | `0x2CE10` | 257 | UnwindData |  |
| 17 | `WHvDeleteVpciDevice` | `0x2CF20` | 279 | UnwindData |  |
| 29 | `WHvGetVpciDeviceInterruptTarget` | `0x2D040` | 163 | UnwindData |  |
| 30 | `WHvGetVpciDeviceNotification` | `0x2D0F0` | 382 | UnwindData |  |
| 31 | `WHvGetVpciDeviceProperty` | `0x2D280` | 475 | UnwindData |  |
| 34 | `WHvMapVpciDeviceInterrupt` | `0x2D470` | 125 | UnwindData |  |
| 35 | `WHvMapVpciDeviceMmioRanges` | `0x2D500` | 90 | UnwindData |  |
| 39 | `WHvReadVpciDeviceRegister` | `0x2D560` | 136 | UnwindData |  |
| 42 | `WHvRequestVpciDeviceInterrupt` | `0x2D5F0` | 175 | UnwindData |  |
| 45 | `WHvRetargetVpciDeviceInterrupt` | `0x2D6B0` | 631 | UnwindData |  |
| 54 | `WHvSetVpciDevicePowerState` | `0x2D930` | 326 | UnwindData |  |
| 61 | `WHvUnmapVpciDeviceInterrupt` | `0x2DA80` | 318 | UnwindData |  |
| 62 | `WHvUnmapVpciDeviceMmioRanges` | `0x2DBD0` | 64 | UnwindData |  |
| 66 | `WHvWriteVpciDeviceRegister` | `0x2DC20` | 136 | UnwindData |  |
| 1 | `WHvAcceptPartitionMigration` | `0x2E450` | 169 | UnwindData |  |
| 2 | `WHvAdviseGpaRange` | `0x2E500` | 241 | UnwindData |  |
| 4 | `WHvCancelPartitionMigration` | `0x2E600` | 108 | UnwindData |  |
| 5 | `WHvCancelRunVirtualProcessor` | `0x2E680` | 136 | UnwindData |  |
| 6 | `WHvCompletePartitionMigration` | `0x2E710` | 108 | UnwindData |  |
| 7 | `WHvCreateNotificationPort` | `0x2E790` | 164 | UnwindData |  |
| 8 | `WHvCreatePartition` | `0x2E840` | 136 | UnwindData |  |
| 9 | `WHvCreateTrigger` | `0x2E8D0` | 242 | UnwindData |  |
| 10 | `WHvCreateVirtualProcessor` | `0x2E9D0` | 127 | UnwindData |  |
| 11 | `WHvCreateVirtualProcessor2` | `0x2EA60` | 216 | UnwindData |  |
| 13 | `WHvDeleteNotificationPort` | `0x2EB40` | 122 | UnwindData |  |
| 14 | `WHvDeletePartition` | `0x2EBC0` | 143 | UnwindData |  |
| 15 | `WHvDeleteTrigger` | `0x2EC60` | 122 | UnwindData |  |
| 16 | `WHvDeleteVirtualProcessor` | `0x2ECE0` | 80 | UnwindData |  |
| 18 | `WHvGetCapability` | `0x2ED40` | 1,969 | UnwindData |  |
| 20 | `WHvGetPartitionCounters` | `0x2F500` | 190 | UnwindData |  |
| 21 | `WHvGetPartitionProperty` | `0x2F5D0` | 178 | UnwindData |  |
| 22 | `WHvGetVirtualProcessorCounters` | `0x2F690` | 294 | UnwindData |  |
| 26 | `WHvGetVirtualProcessorRegisters` | `0x2F7C0` | 335 | UnwindData |  |
| 27 | `WHvGetVirtualProcessorState` | `0x2F920` | 253 | UnwindData |  |
| 32 | `WHvMapGpaRange` | `0x2FA30` | 162 | UnwindData |  |
| 33 | `WHvMapGpaRange2` | `0x2FAE0` | 162 | UnwindData |  |
| 36 | `WHvPostVirtualProcessorSynicMessage` | `0x2FB90` | 333 | UnwindData |  |
| 37 | `WHvQueryGpaRangeDirtyBitmap` | `0x2FCF0` | 142 | UnwindData |  |
| 38 | `WHvReadGpaRange` | `0x2FD90` | 243 | UnwindData |  |
| 40 | `WHvRegisterPartitionDoorbellEvent` | `0x2FE90` | 102 | UnwindData |  |
| 43 | `WHvResetPartition` | `0x2FF00` | 68 | UnwindData |  |
| 44 | `WHvResumePartitionTime` | `0x2FF50` | 68 | UnwindData |  |
| 46 | `WHvRunVirtualProcessor` | `0x2FFA0` | 126 | UnwindData |  |
| 47 | `WHvSetNotificationPortProperty` | `0x30030` | 162 | UnwindData |  |
| 48 | `WHvSetPartitionProperty` | `0x300E0` | 123 | UnwindData |  |
| 51 | `WHvSetVirtualProcessorRegisters` | `0x30170` | 335 | UnwindData |  |
| 52 | `WHvSetVirtualProcessorState` | `0x302D0` | 169 | UnwindData |  |
| 55 | `WHvSetupPartition` | `0x30380` | 85 | UnwindData |  |
| 56 | `WHvSignalVirtualProcessorSynicEvent` | `0x303E0` | 268 | UnwindData |  |
| 57 | `WHvStartPartitionMigration` | `0x30500` | 122 | UnwindData |  |
| 58 | `WHvSuspendPartitionTime` | `0x30580` | 155 | UnwindData |  |
| 59 | `WHvTranslateGva` | `0x30630` | 257 | UnwindData |  |
| 60 | `WHvUnmapGpaRange` | `0x30740` | 163 | UnwindData |  |
| 63 | `WHvUnregisterPartitionDoorbellEvent` | `0x307F0` | 83 | UnwindData |  |
| 64 | `WHvUpdateTriggerParameters` | `0x30850` | 231 | UnwindData |  |
| 65 | `WHvWriteGpaRange` | `0x30940` | 243 | UnwindData |  |
