# Binary Specification: hal.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\hal.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6f8ec8f2fba2ad2ea678fa8e97e6f1ee677f6b99e4868ee2e94ebf175815a5bb`
* **Total Exported Functions:** 91

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `HalAcpiGetTableEx` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAcpiGetTableEx` |
| 2 | `HalAcquireDisplayOwnership` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAcquireDisplayOwnership` |
| 3 | `HalAdjustResourceList` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAdjustResourceList` |
| 4 | `HalAllProcessorsStarted` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAllProcessorsStarted` |
| 5 | `HalAllocateAdapterChannel` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAllocateAdapterChannel` |
| 6 | `HalAllocateCommonBuffer` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAllocateCommonBuffer` |
| 7 | `HalAllocateCrashDumpRegisters` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAllocateCrashDumpRegisters` |
| 8 | `HalAllocateHardwareCounters` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAllocateHardwareCounters` |
| 9 | `HalAssignSlotResources` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalAssignSlotResources` |
| 10 | `HalBugCheckSystem` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalBugCheckSystem` |
| 11 | `HalCalibratePerformanceCounter` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalCalibratePerformanceCounter` |
| 12 | `HalClearSoftwareInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalClearSoftwareInterrupt` |
| 13 | `HalConvertDeviceIdtToIrql` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalConvertDeviceIdtToIrql` |
| 14 | `HalDisableInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalDisableInterrupt` |
| 15 | `HalDisplayString` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalDisplayString` |
| 16 | `HalDmaAllocateCrashDumpRegistersEx` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalDmaAllocateCrashDumpRegistersEx` |
| 17 | `HalDmaFreeCrashDumpRegistersEx` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalDmaFreeCrashDumpRegistersEx` |
| 18 | `HalEnableInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalEnableInterrupt` |
| 19 | `HalEnumerateEnvironmentVariablesEx` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalEnumerateEnvironmentVariablesEx` |
| 20 | `HalEnumerateProcessors` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalEnumerateProcessors` |
| 21 | `HalFlushCommonBuffer` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalFlushCommonBuffer` |
| 22 | `HalFreeCommonBuffer` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalFreeCommonBuffer` |
| 23 | `HalFreeHardwareCounters` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalFreeHardwareCounters` |
| 24 | `HalGetAdapter` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetAdapter` |
| 25 | `HalGetBusData` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetBusData` |
| 26 | `HalGetBusDataByOffset` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetBusDataByOffset` |
| 27 | `HalGetEnvironmentVariable` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetEnvironmentVariable` |
| 28 | `HalGetEnvironmentVariableEx` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetEnvironmentVariableEx` |
| 29 | `HalGetInterruptTargetInformation` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetInterruptTargetInformation` |
| 30 | `HalGetInterruptVector` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetInterruptVector` |
| 31 | `HalGetMemoryCachingRequirements` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetMemoryCachingRequirements` |
| 32 | `HalGetMessageRoutingInfo` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetMessageRoutingInfo` |
| 33 | `HalGetProcessorIdByNtNumber` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetProcessorIdByNtNumber` |
| 34 | `HalGetVectorInput` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalGetVectorInput` |
| 35 | `HalHandleMcheck` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalHandleMcheck` |
| 36 | `HalHandleNMI` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalHandleNMI` |
| 37 | `HalInitSystem` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalInitSystem` |
| 38 | `HalInitializeBios` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalInitializeBios` |
| 39 | `HalInitializeOnResume` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalInitializeOnResume` |
| 40 | `HalInitializeProcessor` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalInitializeProcessor` |
| 41 | `HalIsHyperThreadingEnabled` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalIsHyperThreadingEnabled` |
| 42 | `HalMakeBeep` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalMakeBeep` |
| 43 | `HalPerformEndOfInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalPerformEndOfInterrupt` |
| 44 | `HalProcessorIdle` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalProcessorIdle` |
| 45 | `HalQueryDisplayParameters` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalQueryDisplayParameters` |
| 46 | `HalQueryEnvironmentVariableInfoEx` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalQueryEnvironmentVariableInfoEx` |
| 47 | `HalQueryMaximumProcessorCount` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalQueryMaximumProcessorCount` |
| 48 | `HalQueryRealTimeClock` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalQueryRealTimeClock` |
| 49 | `HalReadDmaCounter` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalReadDmaCounter` |
| 50 | `HalRegisterDynamicProcessor` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalRegisterDynamicProcessor` |
| 51 | `HalRegisterErrataCallbacks` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalRegisterErrataCallbacks` |
| 52 | `HalReportResourceUsage` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalReportResourceUsage` |
| 53 | `HalRequestClockInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalRequestClockInterrupt` |
| 54 | `HalRequestDeferredRecoveryServiceInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalRequestDeferredRecoveryServiceInterrupt` |
| 55 | `HalRequestIpi` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalRequestIpi` |
| 56 | `HalRequestIpiSpecifyVector` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalRequestIpiSpecifyVector` |
| 57 | `HalRequestSoftwareInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalRequestSoftwareInterrupt` |
| 58 | `HalReturnToFirmware` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalReturnToFirmware` |
| 59 | `HalSendNMI` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSendNMI` |
| 60 | `HalSendSoftwareInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSendSoftwareInterrupt` |
| 61 | `HalSetBusData` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSetBusData` |
| 62 | `HalSetBusDataByOffset` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSetBusDataByOffset` |
| 63 | `HalSetDisplayParameters` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSetDisplayParameters` |
| 64 | `HalSetEnvironmentVariable` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSetEnvironmentVariable` |
| 65 | `HalSetEnvironmentVariableEx` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSetEnvironmentVariableEx` |
| 66 | `HalSetProfileInterval` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSetProfileInterval` |
| 67 | `HalSetRealTimeClock` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSetRealTimeClock` |
| 68 | `HalStartDynamicProcessor` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalStartDynamicProcessor` |
| 69 | `HalStartNextProcessor` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalStartNextProcessor` |
| 70 | `HalStartProfileInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalStartProfileInterrupt` |
| 71 | `HalStopProfileInterrupt` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalStopProfileInterrupt` |
| 72 | `HalSystemVectorDispatchEntry` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalSystemVectorDispatchEntry` |
| 73 | `HalTranslateBusAddress` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalTranslateBusAddress` |
| 74 | `HalWheaUpdateCmciPolicy` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.HalWheaUpdateCmciPolicy` |
| 75 | `IoFlushAdapterBuffers` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.IoFlushAdapterBuffers` |
| 76 | `IoFreeAdapterChannel` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.IoFreeAdapterChannel` |
| 77 | `IoFreeMapRegisters` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.IoFreeMapRegisters` |
| 78 | `IoMapTransfer` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.IoMapTransfer` |
| 79 | `IoReadPartitionTable` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.IoReadPartitionTable` |
| 80 | `IoSetPartitionInformation` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.IoSetPartitionInformation` |
| 81 | `IoWritePartitionTable` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.IoWritePartitionTable` |
| 82 | `KdComPortInUse` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.KdComPortInUse` |
| 83 | `KdHvComPortInUse` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.KdHvComPortInUse` |
| 84 | `KeFlushWriteBuffer` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.KeFlushWriteBuffer` |
| 85 | `KeQueryPerformanceCounter` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.KeQueryPerformanceCounter` |
| 86 | `KeStallExecutionProcessor` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.KeStallExecutionProcessor` |
| 87 | `x86BiosAllocateBuffer` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.x86BiosAllocateBuffer` |
| 88 | `x86BiosCall` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.x86BiosCall` |
| 89 | `x86BiosFreeBuffer` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.x86BiosFreeBuffer` |
| 90 | `x86BiosReadMemory` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.x86BiosReadMemory` |
| 91 | `x86BiosWriteMemory` | `0x0` | - | Forwarded | Forwarded to: `ntoskrnl.x86BiosWriteMemory` |
