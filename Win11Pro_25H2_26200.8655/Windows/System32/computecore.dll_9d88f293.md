# Binary Specification: computecore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\computecore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9d88f2938a5dd692778d966046f872ea91b6ef6c128a240b6b76d52cdfb79620`
* **Total Exported Functions:** 67

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `HcsAddResourceToOperation` | `0x13AF0` | 353 | UnwindData |  |
| 7 | `HcsCancelOperation` | `0x13C60` | 326 | UnwindData |  |
| 9 | `HcsCloseOperation` | `0x13DB0` | 16 | UnwindData |  |
| 16 | `HcsCreateOperation` | `0x13DD0` | 19 | UnwindData |  |
| 17 | `HcsCreateOperationWithNotifications` | `0x13DF0` | 395 | UnwindData |  |
| 23 | `HcsGetComputeSystemFromOperation` | `0x13F90` | 21 | UnwindData |  |
| 25 | `HcsGetOperationContext` | `0x13FB0` | 21 | UnwindData |  |
| 26 | `HcsGetOperationId` | `0x13FD0` | 23 | UnwindData |  |
| 27 | `HcsGetOperationProperties` | `0x13FF0` | 330 | UnwindData |  |
| 28 | `HcsGetOperationResult` | `0x14140` | 186 | UnwindData |  |
| 29 | `HcsGetOperationResultAndProcessInfo` | `0x14200` | 181 | UnwindData |  |
| 30 | `HcsGetOperationType` | `0x142C0` | 21 | UnwindData |  |
| 31 | `HcsGetProcessFromOperation` | `0x142E0` | 24 | UnwindData |  |
| 51 | `HcsSetOperationCallback` | `0x14300` | 112 | UnwindData |  |
| 52 | `HcsSetOperationContext` | `0x14380` | 95 | UnwindData |  |
| 65 | `HcsWaitForOperationResult` | `0x143F0` | 182 | UnwindData |  |
| 66 | `HcsWaitForOperationResultAndProcessInfo` | `0x144B0` | 189 | UnwindData |  |
| 10 | `HcsCloseProcess` | `0x14580` | 243 | UnwindData |  |
| 18 | `HcsCreateProcess` | `0x14680` | 806 | UnwindData |  |
| 32 | `HcsGetProcessInfo` | `0x149B0` | 839 | UnwindData |  |
| 33 | `HcsGetProcessProperties` | `0x14D00` | 496 | UnwindData |  |
| 40 | `HcsModifyProcess` | `0x14F00` | 729 | UnwindData |  |
| 44 | `HcsOpenProcess` | `0x151E0` | 524 | UnwindData |  |
| 53 | `HcsSetProcessCallback` | `0x15400` | 347 | UnwindData |  |
| 55 | `HcsSignalProcess` | `0x15570` | 445 | UnwindData |  |
| 63 | `HcsTerminateProcess` | `0x15740` | 448 | UnwindData |  |
| 67 | `HcsWaitForProcessExit` | `0x15910` | 382 | UnwindData |  |
| 35 | `HcsGetServiceProperties` | `0x15AA0` | 323 | UnwindData |  |
| 41 | `HcsModifyServiceSettings` | `0x15BF0` | 212 | UnwindData |  |
| 8 | `HcsCloseComputeSystem` | `0x18720` | 149 | UnwindData |  |
| 11 | `HcsCrashComputeSystem` | `0x187C0` | 297 | UnwindData |  |
| 12 | `HcsCreateComputeSystem` | `0x188F0` | 1,004 | UnwindData |  |
| 13 | `HcsCreateComputeSystemInNamespace` | `0x18CF0` | 163 | UnwindData |  |
| 19 | `HcsEnumerateComputeSystems` | `0x18DA0` | 306 | UnwindData |  |
| 20 | `HcsEnumerateComputeSystemsInNamespace` | `0x18EE0` | 148 | UnwindData |  |
| 21 | `HcsFinalizeLiveMigration` | `0x18F80` | 297 | UnwindData |  |
| 22 | `HcsFinalizeSystemPreservation` | `0x190B0` | 50 | UnwindData |  |
| 24 | `HcsGetComputeSystemProperties` | `0x190F0` | 291 | UnwindData |  |
| 38 | `HcsInitializeLiveMigrationOnSource` | `0x19220` | 297 | UnwindData |  |
| 39 | `HcsModifyComputeSystem` | `0x19350` | 309 | UnwindData |  |
| 42 | `HcsOpenComputeSystem` | `0x19490` | 302 | UnwindData |  |
| 43 | `HcsOpenComputeSystemInNamespace` | `0x195D0` | 148 | UnwindData |  |
| 45 | `HcsPauseComputeSystem` | `0x19670` | 297 | UnwindData |  |
| 46 | `HcsResumeComputeSystem` | `0x197A0` | 297 | UnwindData |  |
| 49 | `HcsSaveComputeSystem` | `0x198D0` | 297 | UnwindData |  |
| 50 | `HcsSetComputeSystemCallback` | `0x19A00` | 211 | UnwindData |  |
| 54 | `HcsShutDownComputeSystem` | `0x19AE0` | 297 | UnwindData |  |
| 56 | `HcsStartComputeSystem` | `0x19C10` | 297 | UnwindData |  |
| 57 | `HcsStartLiveMigrationOnSource` | `0x19D40` | 297 | UnwindData |  |
| 58 | `HcsStartLiveMigrationTransfer` | `0x19E70` | 297 | UnwindData |  |
| 59 | `HcsStartSystemPreservation` | `0x19FA0` | 50 | UnwindData |  |
| 62 | `HcsTerminateComputeSystem` | `0x19FE0` | 297 | UnwindData |  |
| 64 | `HcsWaitForComputeSystemExit` | `0x1A110` | 264 | UnwindData |  |
| 5 | `HcsAbortSystemPreservation` | `0x27110` | 350 | UnwindData |  |
| 14 | `HcsCreateEmptyGuestStateFile` | `0x27280` | 497 | UnwindData |  |
| 15 | `HcsCreateEmptyRuntimeStateFile` | `0x27480` | 253 | UnwindData |  |
| 34 | `HcsGetProcessorCompatibilityFromSavedState` | `0x27590` | 59 | UnwindData |  |
| 36 | `HcsGrantVmAccess` | `0x275E0` | 380 | UnwindData |  |
| 37 | `HcsGrantVmGroupAccess` | `0x27770` | 208 | UnwindData |  |
| 47 | `HcsRevokeVmAccess` | `0x27850` | 384 | UnwindData |  |
| 48 | `HcsRevokeVmGroupAccess` | `0x279E0` | 208 | UnwindData |  |
| 60 | `HcsSubmitWerReport` | `0x27AC0` | 195 | UnwindData |  |
| 1 | `HcsEnumerateVmWorkerProcesses` | `0x27C00` | 333 | UnwindData |  |
| 2 | `HcsFindVmWorkerProcesses` | `0x27D60` | 194 | UnwindData |  |
| 3 | `HcsGetWorkerProcessJob` | `0x27E30` | 277 | UnwindData |  |
| 4 | `HcsStartVmWorkerProcess` | `0x27F50` | 257 | UnwindData |  |
| 61 | `HcsSystemControl` | `0x280B0` | 309 | UnwindData |  |
