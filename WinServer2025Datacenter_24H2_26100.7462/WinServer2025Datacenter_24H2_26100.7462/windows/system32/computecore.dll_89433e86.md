# Binary Specification: computecore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\computecore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `89433e86e079dc0ff91a7f3e339c4b0ab9e0fbd7c26b06d6acc46af280719aea`
* **Total Exported Functions:** 67

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `HcsAddResourceToOperation` | `0x139F0` | 353 | UnwindData |  |
| 7 | `HcsCancelOperation` | `0x13B60` | 326 | UnwindData |  |
| 9 | `HcsCloseOperation` | `0x13CB0` | 16 | UnwindData |  |
| 16 | `HcsCreateOperation` | `0x13CD0` | 19 | UnwindData |  |
| 17 | `HcsCreateOperationWithNotifications` | `0x13CF0` | 395 | UnwindData |  |
| 23 | `HcsGetComputeSystemFromOperation` | `0x13E90` | 21 | UnwindData |  |
| 25 | `HcsGetOperationContext` | `0x13EB0` | 21 | UnwindData |  |
| 26 | `HcsGetOperationId` | `0x13ED0` | 23 | UnwindData |  |
| 27 | `HcsGetOperationProperties` | `0x13EF0` | 330 | UnwindData |  |
| 28 | `HcsGetOperationResult` | `0x14040` | 186 | UnwindData |  |
| 29 | `HcsGetOperationResultAndProcessInfo` | `0x14100` | 181 | UnwindData |  |
| 30 | `HcsGetOperationType` | `0x141C0` | 21 | UnwindData |  |
| 31 | `HcsGetProcessFromOperation` | `0x141E0` | 24 | UnwindData |  |
| 51 | `HcsSetOperationCallback` | `0x14200` | 112 | UnwindData |  |
| 52 | `HcsSetOperationContext` | `0x14280` | 95 | UnwindData |  |
| 65 | `HcsWaitForOperationResult` | `0x142F0` | 182 | UnwindData |  |
| 66 | `HcsWaitForOperationResultAndProcessInfo` | `0x143B0` | 189 | UnwindData |  |
| 10 | `HcsCloseProcess` | `0x14480` | 243 | UnwindData |  |
| 18 | `HcsCreateProcess` | `0x14580` | 806 | UnwindData |  |
| 32 | `HcsGetProcessInfo` | `0x148B0` | 839 | UnwindData |  |
| 33 | `HcsGetProcessProperties` | `0x14C00` | 496 | UnwindData |  |
| 40 | `HcsModifyProcess` | `0x14E00` | 729 | UnwindData |  |
| 44 | `HcsOpenProcess` | `0x150E0` | 524 | UnwindData |  |
| 53 | `HcsSetProcessCallback` | `0x15300` | 347 | UnwindData |  |
| 55 | `HcsSignalProcess` | `0x15470` | 445 | UnwindData |  |
| 63 | `HcsTerminateProcess` | `0x15640` | 448 | UnwindData |  |
| 67 | `HcsWaitForProcessExit` | `0x15810` | 382 | UnwindData |  |
| 35 | `HcsGetServiceProperties` | `0x159A0` | 323 | UnwindData |  |
| 41 | `HcsModifyServiceSettings` | `0x15AF0` | 212 | UnwindData |  |
| 8 | `HcsCloseComputeSystem` | `0x18620` | 149 | UnwindData |  |
| 11 | `HcsCrashComputeSystem` | `0x186C0` | 297 | UnwindData |  |
| 12 | `HcsCreateComputeSystem` | `0x187F0` | 1,004 | UnwindData |  |
| 13 | `HcsCreateComputeSystemInNamespace` | `0x18BF0` | 163 | UnwindData |  |
| 19 | `HcsEnumerateComputeSystems` | `0x18CA0` | 306 | UnwindData |  |
| 20 | `HcsEnumerateComputeSystemsInNamespace` | `0x18DE0` | 148 | UnwindData |  |
| 21 | `HcsFinalizeLiveMigration` | `0x18E80` | 297 | UnwindData |  |
| 22 | `HcsFinalizeSystemPreservation` | `0x18FB0` | 50 | UnwindData |  |
| 24 | `HcsGetComputeSystemProperties` | `0x18FF0` | 291 | UnwindData |  |
| 38 | `HcsInitializeLiveMigrationOnSource` | `0x19120` | 297 | UnwindData |  |
| 39 | `HcsModifyComputeSystem` | `0x19250` | 309 | UnwindData |  |
| 42 | `HcsOpenComputeSystem` | `0x19390` | 302 | UnwindData |  |
| 43 | `HcsOpenComputeSystemInNamespace` | `0x194D0` | 148 | UnwindData |  |
| 45 | `HcsPauseComputeSystem` | `0x19570` | 297 | UnwindData |  |
| 46 | `HcsResumeComputeSystem` | `0x196A0` | 297 | UnwindData |  |
| 49 | `HcsSaveComputeSystem` | `0x197D0` | 297 | UnwindData |  |
| 50 | `HcsSetComputeSystemCallback` | `0x19900` | 211 | UnwindData |  |
| 54 | `HcsShutDownComputeSystem` | `0x199E0` | 297 | UnwindData |  |
| 56 | `HcsStartComputeSystem` | `0x19B10` | 297 | UnwindData |  |
| 57 | `HcsStartLiveMigrationOnSource` | `0x19C40` | 297 | UnwindData |  |
| 58 | `HcsStartLiveMigrationTransfer` | `0x19D70` | 297 | UnwindData |  |
| 59 | `HcsStartSystemPreservation` | `0x19EA0` | 50 | UnwindData |  |
| 62 | `HcsTerminateComputeSystem` | `0x19EE0` | 297 | UnwindData |  |
| 64 | `HcsWaitForComputeSystemExit` | `0x1A010` | 264 | UnwindData |  |
| 5 | `HcsAbortSystemPreservation` | `0x27000` | 350 | UnwindData |  |
| 14 | `HcsCreateEmptyGuestStateFile` | `0x27170` | 497 | UnwindData |  |
| 15 | `HcsCreateEmptyRuntimeStateFile` | `0x27370` | 253 | UnwindData |  |
| 34 | `HcsGetProcessorCompatibilityFromSavedState` | `0x27480` | 59 | UnwindData |  |
| 36 | `HcsGrantVmAccess` | `0x274D0` | 380 | UnwindData |  |
| 37 | `HcsGrantVmGroupAccess` | `0x27660` | 208 | UnwindData |  |
| 47 | `HcsRevokeVmAccess` | `0x27740` | 384 | UnwindData |  |
| 48 | `HcsRevokeVmGroupAccess` | `0x278D0` | 208 | UnwindData |  |
| 60 | `HcsSubmitWerReport` | `0x279B0` | 195 | UnwindData |  |
| 1 | `HcsEnumerateVmWorkerProcesses` | `0x27AF0` | 333 | UnwindData |  |
| 2 | `HcsFindVmWorkerProcesses` | `0x27C50` | 194 | UnwindData |  |
| 3 | `HcsGetWorkerProcessJob` | `0x27D20` | 277 | UnwindData |  |
| 4 | `HcsStartVmWorkerProcess` | `0x27E40` | 257 | UnwindData |  |
| 61 | `HcsSystemControl` | `0x27FA0` | 309 | UnwindData |  |
