# Binary Specification: d3d10level9.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\d3d10level9.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b914a1d7f5dfd8d8d0e0b8d6c4e464e48832c243377eda8c0d27fb37d8f6cd5b`
* **Total Exported Functions:** 113

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 67 | `D3DKMTGetDeviceState` | `0xCEA0` | 960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `D3DKMTLock` | `0xD260` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `D3DKMTUnlock` | `0xD360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `D3DKMTPresent` | `0xD380` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `D3DKMTSignalSynchronizationObjectFromGpu2` | `0xD640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `D3DKMTRender` | `0xD660` | 6,336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `D3DKMTCreateAllocation` | `0xEF20` | 12,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `D3D10CheckLevel9Hardware` | `0x11EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `D3D10Level9DumpJournal` | `0x11EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `D3D11CreateDeviceExternalImplementation` | `0x11F00` | 534 | UnwindData |  |
| 43 | `RetrieveFilteredOpenAdapter` | `0x168B0` | 28,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `LogMarkerStringTable` | `0x1D7E0` | 145 | UnwindData |  |
| 41 | `OpenAdapter10` | `0x1DAE0` | 106 | UnwindData |  |
| 42 | `OpenAdapter10_2` | `0x1DB50` | 109 | UnwindData |  |
| 4 | `D3DKMTChangeVideoMemoryReservation` | `0x273A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `D3DKMTConfigureSharedResource` | `0x273C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `D3DKMTDestroyAllocation2` | `0x273E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `D3DKMTDestroyContext` | `0x27400` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `D3DKMTDestroyDevice` | `0x27420` | 71 | UnwindData |  |
| 9 | `D3DKMTDestroyKeyedMutex` | `0x27470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `D3DKMTDestroySynchronizationObject` | `0x27490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `D3DKMTFreeGpuVirtualAddress` | `0x274B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `D3DKMTGetAllocationPriority` | `0x274D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `D3DKMTGetThunkVersion` | `0x274F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `D3DKMTInvalidateCache` | `0x27500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `D3DKMTOfferAllocations` | `0x27520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `D3DKMTOutputDuplPresent` | `0x27540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `D3DKMTPinDirectFlipResources` | `0x27560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `D3DKMTPresentMultiPlaneOverlay2` | `0x27580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `D3DKMTPresentMultiPlaneOverlay` | `0x275A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `D3DKMTReclaimAllocations` | `0x275C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `D3DKMTSetContextInProcessSchedulingPriority` | `0x275E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `D3DKMTSetDisplayPrivateDriverFormat` | `0x27600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `D3DKMTSetQueuedLimit` | `0x27620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `D3DKMTSetStablePowerState` | `0x27640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `D3DKMTSetVidPnSourceOwner1` | `0x27660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `D3DKMTSignalSynchronizationObject2` | `0x27680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `D3DKMTSignalSynchronizationObject` | `0x276A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `D3DKMTSignalSynchronizationObjectFromCpu` | `0x276C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `D3DKMTSignalSynchronizationObjectFromGpu` | `0x276E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `D3DKMTSubmitCommand` | `0x27700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `D3DKMTUnlock2` | `0x27720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `D3DKMTUnpinDirectFlipResources` | `0x27740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `D3DKMTUpdateGpuVirtualAddress` | `0x27760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `D3DKMTWaitForSynchronizationObject2` | `0x27780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `D3DKMTWaitForSynchronizationObject` | `0x277A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `D3DKMTWaitForSynchronizationObjectFromCpu` | `0x277C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `D3DKMTWaitForSynchronizationObjectFromGpu` | `0x277E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `D3DKMTWaitForVerticalBlankEvent2` | `0x27800` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `D3DKMTAcquireKeyedMutex` | `0x27D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `D3DKMTAcquireKeyedMutex2` | `0x27D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `D3DKMTCheckMultiPlaneOverlaySupport` | `0x27D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `D3DKMTCheckMultiPlaneOverlaySupport2` | `0x27DB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `D3DKMTCloseAdapter` | `0x27DD0` | 75 | UnwindData |  |
| 50 | `D3DKMTCreateAllocation2` | `0x27E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `D3DKMTCreateContext` | `0x27E50` | 55 | UnwindData |  |
| 52 | `D3DKMTCreateContextVirtual` | `0x27E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `D3DKMTCreateDevice` | `0x27EB0` | 135 | UnwindData |  |
| 54 | `D3DKMTCreateKeyedMutex` | `0x27F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `D3DKMTCreateKeyedMutex2` | `0x27F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `D3DKMTCreatePagingQueue` | `0x27F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `D3DKMTCreateSynchronizationObject` | `0x27FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `D3DKMTCreateSynchronizationObject2` | `0x27FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `D3DKMTDestroyAllocation` | `0x27FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `D3DKMTDestroyPagingQueue` | `0x28000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `D3DKMTEscape` | `0x28020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `D3DKMTEvict` | `0x28040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `D3DKMTFlushHeapTransitions` | `0x28060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `D3DKMTGetContextInProcessSchedulingPriority` | `0x28080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `D3DKMTGetContextSchedulingPriority` | `0x280A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `D3DKMTGetDeviceSchedulingPriority` | `0x280A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `D3DKMTGetDisplayModeList` | `0x280C0` | 594 | UnwindData |  |
| 69 | `D3DKMTGetMultisampleMethodList` | `0x28320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `D3DKMTGetResourcePresentPrivateDriverData` | `0x28340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `D3DKMTGetRuntimeData` | `0x28360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `D3DKMTGetSharedPrimaryHandle` | `0x28380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `D3DKMTLock2` | `0x28390` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `D3DKMTMakeResident` | `0x283B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `D3DKMTMapGpuVirtualAddress` | `0x283D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `D3DKMTMarkDeviceAsError` | `0x283F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `D3DKMTOpenAdapterFromDeviceName` | `0x28410` | 96 | UnwindData |  |
| 79 | `D3DKMTOpenAdapterFromGdiDisplayName` | `0x28480` | 602 | UnwindData |  |
| 80 | `D3DKMTOpenKeyedMutex` | `0x286E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `D3DKMTOpenKeyedMutex2` | `0x28700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `D3DKMTOpenNtHandleFromName` | `0x28720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `D3DKMTOpenResource` | `0x28740` | 58 | UnwindData |  |
| 84 | `D3DKMTOpenResource2` | `0x28780` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `D3DKMTOpenResourceFromNtHandle` | `0x287A0` | 58 | UnwindData |  |
| 86 | `D3DKMTOpenSyncObjectFromNtHandle` | `0x287E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `D3DKMTOpenSyncObjectFromNtHandle2` | `0x28800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `D3DKMTOpenSyncObjectNtHandleFromName` | `0x28820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `D3DKMTOpenSynchronizationObject` | `0x28840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `D3DKMTQueryAdapterInfo` | `0x28860` | 128 | UnwindData |  |
| 92 | `D3DKMTQueryAllocationResidency` | `0x288F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `D3DKMTQueryClockCalibration` | `0x28910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `D3DKMTQueryResourceInfo` | `0x28930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `D3DKMTQueryResourceInfoFromNtHandle` | `0x28950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `D3DKMTQueryVideoMemoryInfo` | `0x28970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `D3DKMTReclaimAllocations2` | `0x28990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `D3DKMTRegisterTrimNotification` | `0x289B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `D3DKMTReleaseKeyedMutex` | `0x289D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `D3DKMTReleaseKeyedMutex2` | `0x289F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `D3DKMTReserveGpuVirtualAddress` | `0x28A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `D3DKMTSetAllocationPriority` | `0x28A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `D3DKMTSetContextSchedulingPriority` | `0x28A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `D3DKMTSetDeviceSchedulingPriority` | `0x28A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `D3DKMTSetDisplayMode` | `0x28A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `D3DKMTSetGammaRamp` | `0x28A90` | 429 | UnwindData |  |
| 108 | `D3DKMTSetVidPnSourceOwner` | `0x28C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `D3DKMTShareObjects` | `0x28C70` | 32 | UnwindData |  |
| 111 | `D3DKMTUnregisterTrimNotification` | `0x28CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `D3DKMTUpdateAllocationProperty` | `0x28CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `D3DKMTWaitForVerticalBlankEvent` | `0x28CE0` | 131,788 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
