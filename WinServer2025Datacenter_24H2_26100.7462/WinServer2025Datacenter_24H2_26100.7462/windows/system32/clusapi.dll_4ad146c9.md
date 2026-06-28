# Binary Specification: clusapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\clusapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4ad146c9870c76f3a8928ebcb9adc65c4158c8c203cdc648e03cb1aa169907c7`
* **Total Exported Functions:** 396

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `BackupClusterDatabase` | `0x2AD60` | 28 | UnwindData |  |
| 388 | `SetClusterNetworkPriorityOrder` | `0x2AD60` | 28 | UnwindData |  |
| 33 | `CloseCluster` | `0x2AD90` | 514 | UnwindData |  |
| 49 | `ClusapiSetReasonHandler` | `0x2AFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ClusterCaptureLiveDump` | `0x2AFC0` | 162 | UnwindData |  |
| 57 | `ClusterCaptureLiveDumpEx` | `0x2B070` | 610 | UnwindData |  |
| 59 | `ClusterCloseEnum` | `0x2B2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ClusterCloseEnumEx` | `0x2B2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ClusterEnum` | `0x2B300` | 182 | UnwindData |  |
| 76 | `ClusterEnumEx` | `0x2B3C0` | 88 | UnwindData |  |
| 83 | `ClusterGetEnumCount` | `0x2B420` | 35 | UnwindData |  |
| 84 | `ClusterGetEnumCountEx` | `0x2B450` | 40 | UnwindData |  |
| 91 | `ClusterGetMaximumAccessForToken` | `0x2B480` | 140 | UnwindData |  |
| 94 | `ClusterGroupCloseEnum` | `0x2B520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `ClusterGroupCloseEnumEx` | `0x2B530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `ClusterGroupEnum` | `0x2B540` | 182 | UnwindData |  |
| 99 | `ClusterGroupEnumEx` | `0x2B600` | 558 | UnwindData |  |
| 100 | `ClusterGroupGetEnumCount` | `0x2B840` | 35 | UnwindData |  |
| 101 | `ClusterGroupGetEnumCountEx` | `0x2B870` | 35 | UnwindData |  |
| 102 | `ClusterGroupOpenEnum` | `0x2B8A0` | 189 | UnwindData |  |
| 103 | `ClusterGroupOpenEnumEx` | `0x2B970` | 257 | UnwindData |  |
| 104 | `ClusterGroupSetCloseEnum` | `0x2BA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `ClusterGroupSetEnum` | `0x2BA90` | 163 | UnwindData |  |
| 108 | `ClusterGroupSetGetEnumCount` | `0x2BB40` | 35 | UnwindData |  |
| 109 | `ClusterGroupSetOpenEnum` | `0x2BB70` | 162 | UnwindData |  |
| 119 | `ClusterNetInterfaceCloseEnum` | `0x2BC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `ClusterNetInterfaceEnum` | `0x2BC30` | 176 | UnwindData |  |
| 123 | `ClusterNetInterfaceOpenEnum` | `0x2BCF0` | 225 | UnwindData |  |
| 129 | `ClusterNetworkHealthFreeInterfaceConnections` | `0x2BDE0` | 98 | UnwindData |  |
| 130 | `ClusterNetworkHealthFreeNodeConnections` | `0x2BDE0` | 98 | UnwindData |  |
| 131 | `ClusterNetworkHealthGetInterfaceConnections` | `0x2BE50` | 613 | UnwindData |  |
| 132 | `ClusterNetworkHealthGetNodeConnections` | `0x2C0C0` | 1,415 | UnwindData |  |
| 134 | `ClusterNodeCloseEnum` | `0x2C650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `ClusterNodeCloseEnumEx` | `0x2C660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `ClusterNodeEnum` | `0x2C670` | 182 | UnwindData |  |
| 139 | `ClusterNodeEnumEx` | `0x2C730` | 88 | UnwindData |  |
| 140 | `ClusterNodeGetEnumCount` | `0x2C790` | 35 | UnwindData |  |
| 141 | `ClusterNodeGetEnumCountEx` | `0x2C7C0` | 40 | UnwindData |  |
| 142 | `ClusterNodeOpenEnum` | `0x2C7F0` | 202 | UnwindData |  |
| 143 | `ClusterNodeOpenEnumEx` | `0x2C8C0` | 220 | UnwindData |  |
| 145 | `ClusterOpenEnum` | `0x2C9B0` | 258 | UnwindData |  |
| 146 | `ClusterOpenEnumEx` | `0x2CAC0` | 300 | UnwindData |  |
| 192 | `ClusterResourceCloseEnumEx` | `0x2CC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `ClusterResourceEnumEx` | `0x2CC10` | 600 | UnwindData |  |
| 200 | `ClusterResourceGetEnumCountEx` | `0x2CE70` | 35 | UnwindData |  |
| 202 | `ClusterResourceOpenEnumEx` | `0x2CEA0` | 265 | UnwindData |  |
| 214 | `ClusterSetAccountAccess` | `0x2CFB0` | 1,152 | UnwindData |  |
| 218 | `ClusterSharedVolumeClearBackupState` | `0x2D440` | 45 | UnwindData |  |
| 219 | `ClusterSharedVolumeSetSnapshotState` | `0x2D480` | 348 | UnwindData |  |
| 221 | `ClusterUpgradeFunctionalLevel` | `0x2D5F0` | 1,191 | UnwindData |  |
| 222 | `ClusterUpgradeFunctionalLevelEx` | `0x2DAA0` | 1,141 | UnwindData |  |
| 223 | `ClusterWprAddMarker` | `0x2DF20` | 283 | UnwindData |  |
| 224 | `ClusterWprCancel` | `0x2E050` | 253 | UnwindData |  |
| 225 | `ClusterWprCaptureState` | `0x2E160` | 283 | UnwindData |  |
| 226 | `ClusterWprFlush` | `0x2E290` | 283 | UnwindData |  |
| 227 | `ClusterWprFlush2` | `0x2E3C0` | 324 | UnwindData |  |
| 228 | `ClusterWprStart` | `0x2E510` | 342 | UnwindData |  |
| 229 | `ClusterWprStop` | `0x2E670` | 283 | UnwindData |  |
| 230 | `ClusterWprStop2` | `0x2E7A0` | 324 | UnwindData |  |
| 283 | `GetClusterInformation` | `0x2E9E0` | 645 | UnwindData |  |
| 296 | `GetClusterQuorumResource` | `0x2EC70` | 407 | UnwindData |  |
| 302 | `GetClusterSharedVolumeNameForFile` | `0x2EE10` | 815 | UnwindData |  |
| 305 | `GetNodeClusterState` | `0x2F150` | 219 | UnwindData |  |
| 318 | `IsFileOnClusterSharedVolume` | `0x2F240` | 346 | UnwindData |  |
| 334 | `OpenCluster` | `0x2F3A0` | 34 | UnwindData |  |
| 335 | `OpenClusterEx` | `0x2F3D0` | 33 | UnwindData |  |
| 336 | `OpenClusterEx2` | `0x2F400` | 27 | UnwindData |  |
| 374 | `RestoreClusterDatabase` | `0x2F430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `SetClusterServiceAccountPassword` | `0x2F430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `SetClusterName` | `0x2F440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `SetClusterNameEx` | `0x2F450` | 523 | UnwindData |  |
| 389 | `SetClusterQuorumResource` | `0x2F670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `SetClusterQuorumResourceEx` | `0x2F680` | 226 | UnwindData |  |
| 22 | `AddClusterStorageNode` | `0x38C70` | 12,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `RemoveClusterStorageNode` | `0x38C70` | 12,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetClusterUserMgrResource` | `0x3BBA0` | 277 | UnwindData |  |
| 16 | `AddClusterNode` | `0x42750` | 26 | UnwindData |  |
| 17 | `AddClusterNodeEx` | `0x42770` | 5,474 | UnwindData |  |
| 144 | `ClusterNodeReplacement` | `0x43CE0` | 435 | UnwindData |  |
| 231 | `CreateCluster` | `0x43EA0` | 49 | UnwindData |  |
| 236 | `CreateClusterManagementPoint` | `0x43EE0` | 260 | UnwindData |  |
| 237 | `CreateClusterNameAccount` | `0x43FF0` | 8,982 | UnwindData |  |
| 253 | `DestroyCluster` | `0x46310` | 3,441 | UnwindData |  |
| 256 | `DetermineCNOResTypeFromCluster` | `0x47090` | 105 | UnwindData |  |
| 257 | `DetermineCNOResTypeFromNodelist` | `0x47100` | 107 | UnwindData |  |
| 258 | `DetermineClusterCloudTypeFromCluster` | `0x47180` | 189 | UnwindData |  |
| 259 | `DetermineClusterCloudTypeFromNodelist` | `0x47250` | 184 | UnwindData |  |
| 303 | `GetClusterUserMgrCredential` | `0x47310` | 1,972 | UnwindData |  |
| 304 | `GetNodeCloudTypeDW` | `0x47AD0` | 82 | UnwindData |  |
| 363 | `RemoveClusterNameAccount` | `0x47B30` | 2,300 | UnwindData |  |
| 10 | `AddClusterGroupDependency` | `0x4DE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `AddClusterGroupDependencyEx` | `0x4DEA0` | 217 | UnwindData |  |
| 29 | `CancelClusterGroupOperation` | `0x4DF80` | 85 | UnwindData |  |
| 34 | `CloseClusterGroup` | `0x4DFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `CreateClusterGroup` | `0x4DFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `CreateClusterGroupEx` | `0x4E000` | 618 | UnwindData |  |
| 245 | `DeleteClusterGroup` | `0x4E270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `DeleteClusterGroupEx` | `0x4E280` | 186 | UnwindData |  |
| 254 | `DestroyClusterGroup` | `0x4E340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `DestroyClusterGroupEx` | `0x4E350` | 192 | UnwindData |  |
| 276 | `GetClusterFromGroup` | `0x4E420` | 94 | UnwindData |  |
| 282 | `GetClusterGroupState` | `0x4E490` | 317 | UnwindData |  |
| 319 | `MoveClusterGroup` | `0x4E5E0` | 32 | UnwindData |  |
| 320 | `MoveClusterGroupEx` | `0x4E610` | 29 | UnwindData |  |
| 321 | `MoveClusterGroupEx2` | `0x4E640` | 746 | UnwindData |  |
| 322 | `OfflineClusterGroup` | `0x4E930` | 29 | UnwindData |  |
| 323 | `OfflineClusterGroupEx` | `0x4E960` | 21 | UnwindData |  |
| 324 | `OfflineClusterGroupEx2` | `0x4E980` | 251 | UnwindData |  |
| 328 | `OnlineClusterGroup` | `0x4EA90` | 374 | UnwindData |  |
| 329 | `OnlineClusterGroupEx` | `0x4EC10` | 29 | UnwindData |  |
| 330 | `OnlineClusterGroupEx2` | `0x4EC40` | 516 | UnwindData |  |
| 337 | `OpenClusterGroup` | `0x4EE50` | 32 | UnwindData |  |
| 338 | `OpenClusterGroupEx` | `0x4EE80` | 31 | UnwindData |  |
| 357 | `RemoveClusterGroupDependency` | `0x4EEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `RemoveClusterGroupDependencyEx` | `0x4EEC0` | 217 | UnwindData |  |
| 378 | `SetClusterGroupName` | `0x4EFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `SetClusterGroupNameEx` | `0x4EFB0` | 197 | UnwindData |  |
| 380 | `SetClusterGroupNodeList` | `0x4F080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `SetClusterGroupNodeListEx` | `0x4F090` | 694 | UnwindData |  |
| 395 | `SetGroupDependencyExpression` | `0x4F350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `SetGroupDependencyExpressionEx` | `0x4F360` | 197 | UnwindData |  |
| 36 | `CloseClusterNetInterface` | `0x501D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `GetClusterFromNetInterface` | `0x501E0` | 84 | UnwindData |  |
| 285 | `GetClusterNetInterface` | `0x50240` | 285 | UnwindData |  |
| 287 | `GetClusterNetInterfaceState` | `0x50370` | 112 | UnwindData |  |
| 340 | `OpenClusterNetInterface` | `0x503F0` | 32 | UnwindData |  |
| 341 | `OpenClusterNetInterfaceEx` | `0x50420` | 31 | UnwindData |  |
| 61 | `ClusterControl` | `0x568A0` | 69 | UnwindData |  |
| 62 | `ClusterControlEx` | `0x568F0` | 609 | UnwindData |  |
| 96 | `ClusterGroupControl` | `0x56B60` | 69 | UnwindData |  |
| 97 | `ClusterGroupControlEx` | `0x56BB0` | 572 | UnwindData |  |
| 105 | `ClusterGroupSetControl` | `0x56E00` | 69 | UnwindData |  |
| 106 | `ClusterGroupSetControlEx` | `0x56E50` | 560 | UnwindData |  |
| 120 | `ClusterNetInterfaceControl` | `0x57090` | 69 | UnwindData |  |
| 121 | `ClusterNetInterfaceControlEx` | `0x570E0` | 572 | UnwindData |  |
| 125 | `ClusterNetworkControl` | `0x57330` | 69 | UnwindData |  |
| 126 | `ClusterNetworkControlEx` | `0x57380` | 572 | UnwindData |  |
| 136 | `ClusterNodeControl` | `0x575D0` | 69 | UnwindData |  |
| 137 | `ClusterNodeControlEx` | `0x57620` | 676 | UnwindData |  |
| 193 | `ClusterResourceControl` | `0x578D0` | 74 | UnwindData |  |
| 194 | `ClusterResourceControlAsUser` | `0x57920` | 69 | UnwindData |  |
| 195 | `ClusterResourceControlAsUserEx` | `0x57970` | 97 | UnwindData |  |
| 196 | `ClusterResourceControlEx` | `0x579E0` | 81 | UnwindData |  |
| 204 | `ClusterResourceTypeControl` | `0x57A40` | 86 | UnwindData |  |
| 205 | `ClusterResourceTypeControlAsUser` | `0x57AA0` | 86 | UnwindData |  |
| 206 | `ClusterResourceTypeControlAsUserEx` | `0x57B00` | 93 | UnwindData |  |
| 207 | `ClusterResourceTypeControlEx` | `0x57B70` | 93 | UnwindData |  |
| 37 | `CloseClusterNetwork` | `0x59030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `ClusterNetworkCloseEnum` | `0x59040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `ClusterNetworkEnum` | `0x59050` | 182 | UnwindData |  |
| 128 | `ClusterNetworkGetEnumCount` | `0x59110` | 35 | UnwindData |  |
| 133 | `ClusterNetworkOpenEnum` | `0x59140` | 189 | UnwindData |  |
| 278 | `GetClusterFromNetwork` | `0x59210` | 81 | UnwindData |  |
| 288 | `GetClusterNetworkId` | `0x59270` | 205 | UnwindData |  |
| 290 | `GetClusterNetworkState` | `0x59350` | 112 | UnwindData |  |
| 342 | `OpenClusterNetwork` | `0x593D0` | 32 | UnwindData |  |
| 343 | `OpenClusterNetworkEx` | `0x59400` | 31 | UnwindData |  |
| 386 | `SetClusterNetworkName` | `0x59430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `SetClusterNetworkNameEx` | `0x59440` | 197 | UnwindData |  |
| 38 | `CloseClusterNode` | `0x5B610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `EvictClusterNode` | `0x5B620` | 33 | UnwindData |  |
| 261 | `EvictClusterNodeEx` | `0x5B650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `EvictClusterNodeEx2` | `0x5B660` | 1,181 | UnwindData |  |
| 279 | `GetClusterFromNode` | `0x5BB10` | 84 | UnwindData |  |
| 291 | `GetClusterNodeId` | `0x5BB70` | 229 | UnwindData |  |
| 293 | `GetClusterNodeState` | `0x5BC60` | 128 | UnwindData |  |
| 344 | `OpenClusterNode` | `0x5BCF0` | 32 | UnwindData |  |
| 345 | `OpenClusterNodeById` | `0x5BD20` | 1,440 | UnwindData |  |
| 346 | `OpenClusterNodeEx` | `0x5C2D0` | 31 | UnwindData |  |
| 350 | `PauseClusterNode` | `0x5C300` | 29 | UnwindData |  |
| 351 | `PauseClusterNodeEx` | `0x5C330` | 21 | UnwindData |  |
| 352 | `PauseClusterNodeEx2` | `0x5C350` | 887 | UnwindData |  |
| 375 | `ResumeClusterNode` | `0x5C6D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `ResumeClusterNodeEx` | `0x5C6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `ResumeClusterNodeEx2` | `0x5C700` | 597 | UnwindData |  |
| 39 | `CloseClusterNotifyPort` | `0x61E50` | 122 | UnwindData |  |
| 238 | `CreateClusterNotifyPort` | `0x61ED0` | 497 | UnwindData |  |
| 239 | `CreateClusterNotifyPortV2` | `0x620D0` | 694 | UnwindData |  |
| 294 | `GetClusterNotify` | `0x62390` | 471 | UnwindData |  |
| 295 | `GetClusterNotifyV2` | `0x62570` | 1,055 | UnwindData |  |
| 306 | `GetNotifyEventHandle` | `0x629A0` | 167 | UnwindData |  |
| 353 | `RegisterClusterNotify` | `0x62A50` | 541 | UnwindData |  |
| 354 | `RegisterClusterNotifyV2` | `0x62C80` | 104 | UnwindData |  |
| 355 | `RegisterClusterResourceTypeNotifyV2` | `0x62CF0` | 100 | UnwindData |  |
| 77 | `ClusterFreeMemory` | `0x67980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `ClusterRegCloseKey` | `0x679A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `ClusterRegCreateKey` | `0x679B0` | 53 | UnwindData |  |
| 160 | `ClusterRegCreateKeyEx` | `0x679F0` | 804 | UnwindData |  |
| 161 | `ClusterRegCreateKeyForceSync` | `0x67D20` | 123 | UnwindData |  |
| 163 | `ClusterRegDeleteKey` | `0x67DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `ClusterRegDeleteKeyEx` | `0x67DC0` | 197 | UnwindData |  |
| 165 | `ClusterRegDeleteKeyForceSync` | `0x67E90` | 76 | UnwindData |  |
| 166 | `ClusterRegDeleteValue` | `0x67EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `ClusterRegDeleteValueEx` | `0x67F00` | 197 | UnwindData |  |
| 168 | `ClusterRegDeleteValueForceSync` | `0x67FD0` | 76 | UnwindData |  |
| 169 | `ClusterRegEnumKey` | `0x68030` | 238 | UnwindData |  |
| 170 | `ClusterRegEnumValue` | `0x68130` | 355 | UnwindData |  |
| 172 | `ClusterRegGetKeySecurity` | `0x682A0` | 143 | UnwindData |  |
| 173 | `ClusterRegOpenKey` | `0x68340` | 494 | UnwindData |  |
| 174 | `ClusterRegQueryAllValues` | `0x68540` | 105 | UnwindData |  |
| 175 | `ClusterRegQueryInfoKey` | `0x685B0` | 308 | UnwindData |  |
| 176 | `ClusterRegQueryValue` | `0x686F0` | 224 | UnwindData |  |
| 179 | `ClusterRegSetKeySecurity` | `0x687E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `ClusterRegSetKeySecurityEx` | `0x687F0` | 267 | UnwindData |  |
| 181 | `ClusterRegSetValue` | `0x68910` | 29 | UnwindData |  |
| 182 | `ClusterRegSetValueEx` | `0x68940` | 232 | UnwindData |  |
| 183 | `ClusterRegSetValueForceSync` | `0x68A30` | 105 | UnwindData |  |
| 184 | `ClusterRegSyncDatabase` | `0x68AA0` | 84 | UnwindData |  |
| 281 | `GetClusterGroupKey` | `0x68B00` | 221 | UnwindData |  |
| 284 | `GetClusterKey` | `0x68BF0` | 344 | UnwindData |  |
| 286 | `GetClusterNetInterfaceKey` | `0x68D50` | 221 | UnwindData |  |
| 289 | `GetClusterNetworkKey` | `0x68E40` | 222 | UnwindData |  |
| 292 | `GetClusterNodeKey` | `0x68F30` | 284 | UnwindData |  |
| 298 | `GetClusterResourceKey` | `0x69060` | 221 | UnwindData |  |
| 301 | `GetClusterResourceTypeKey` | `0x69150` | 26,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `AddClusterResourceDependency` | `0x6F700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `AddClusterResourceDependencyEx` | `0x6F710` | 242 | UnwindData |  |
| 20 | `AddClusterResourceNode` | `0x6F810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `AddClusterResourceNodeEx` | `0x6F820` | 301 | UnwindData |  |
| 24 | `AddResourceToClusterSharedVolumes` | `0x6F960` | 90 | UnwindData |  |
| 25 | `AddResourceToClusterSharedVolumesEx` | `0x6F9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `AddResourceToClusterSharedVolumesEx2` | `0x6F9D0` | 252 | UnwindData |  |
| 28 | `CanResourceBeDependent` | `0x6FAE0` | 139 | UnwindData |  |
| 30 | `ChangeClusterResourceGroup` | `0x6FB80` | 120 | UnwindData |  |
| 31 | `ChangeClusterResourceGroupEx` | `0x6FC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ChangeClusterResourceGroupEx2` | `0x6FC10` | 324 | UnwindData |  |
| 40 | `CloseClusterResource` | `0x6FD60` | 549 | UnwindData |  |
| 191 | `ClusterResourceCloseEnum` | `0x6FF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `ClusterResourceEnum` | `0x6FFA0` | 189 | UnwindData |  |
| 199 | `ClusterResourceGetEnumCount` | `0x70070` | 49 | UnwindData |  |
| 201 | `ClusterResourceOpenEnum` | `0x700B0` | 189 | UnwindData |  |
| 203 | `ClusterResourceTypeCloseEnum` | `0x70180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `ClusterResourceTypeEnum` | `0x70190` | 206 | UnwindData |  |
| 209 | `ClusterResourceTypeGetEnumCount` | `0x70270` | 49 | UnwindData |  |
| 210 | `ClusterResourceTypeOpenEnum` | `0x702B0` | 213 | UnwindData |  |
| 240 | `CreateClusterResource` | `0x70390` | 21 | UnwindData |  |
| 241 | `CreateClusterResourceEx` | `0x703B0` | 406 | UnwindData |  |
| 242 | `CreateClusterResourceType` | `0x70550` | 37 | UnwindData |  |
| 243 | `CreateClusterResourceTypeEx` | `0x70580` | 295 | UnwindData |  |
| 244 | `CreateClusterResourceWithId` | `0x706B0` | 23 | UnwindData |  |
| 249 | `DeleteClusterResource` | `0x70880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `DeleteClusterResourceEx` | `0x70890` | 157 | UnwindData |  |
| 251 | `DeleteClusterResourceType` | `0x70940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `DeleteClusterResourceTypeEx` | `0x70950` | 248 | UnwindData |  |
| 263 | `FailClusterResource` | `0x70A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `FailClusterResourceEx` | `0x70A60` | 185 | UnwindData |  |
| 280 | `GetClusterFromResource` | `0x70B20` | 94 | UnwindData |  |
| 297 | `GetClusterResourceDependencyExpression` | `0x70B90` | 260 | UnwindData |  |
| 299 | `GetClusterResourceNetworkName` | `0x70CA0` | 293 | UnwindData |  |
| 300 | `GetClusterResourceState` | `0x70DD0` | 406 | UnwindData |  |
| 325 | `OfflineClusterResource` | `0x70F70` | 82 | UnwindData |  |
| 326 | `OfflineClusterResourceEx` | `0x70FD0` | 21 | UnwindData |  |
| 327 | `OfflineClusterResourceEx2` | `0x70FF0` | 263 | UnwindData |  |
| 331 | `OnlineClusterResource` | `0x71100` | 82 | UnwindData |  |
| 332 | `OnlineClusterResourceEx` | `0x71160` | 21 | UnwindData |  |
| 333 | `OnlineClusterResourceEx2` | `0x71180` | 263 | UnwindData |  |
| 347 | `OpenClusterResource` | `0x71290` | 32 | UnwindData |  |
| 348 | `OpenClusterResourceEx` | `0x712C0` | 31 | UnwindData |  |
| 364 | `RemoveClusterResourceDependency` | `0x712F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `RemoveClusterResourceDependencyEx` | `0x71300` | 242 | UnwindData |  |
| 366 | `RemoveClusterResourceNode` | `0x71400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `RemoveClusterResourceNodeEx` | `0x71410` | 301 | UnwindData |  |
| 370 | `RemoveResourceFromClusterSharedVolumes` | `0x71550` | 87 | UnwindData |  |
| 372 | `RestartClusterResource` | `0x715B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `RestartClusterResourceEx` | `0x715C0` | 208 | UnwindData |  |
| 391 | `SetClusterResourceDependencyExpression` | `0x716A0` | 99 | UnwindData |  |
| 392 | `SetClusterResourceName` | `0x71710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `SetClusterResourceNameEx` | `0x71720` | 213 | UnwindData |  |
| 148 | `ClusterRegBatchCloseNotification` | `0x724F0` | 135 | UnwindData |  |
| 149 | `ClusterRegBatchReadCommand` | `0x72580` | 98 | UnwindData |  |
| 150 | `ClusterRegCloseBatch` | `0x725F0` | 266 | UnwindData |  |
| 151 | `ClusterRegCloseBatchEx` | `0x72700` | 99 | UnwindData |  |
| 152 | `ClusterRegCloseBatchNotifyPort` | `0x72770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `ClusterRegCloseReadBatch` | `0x72780` | 282 | UnwindData |  |
| 155 | `ClusterRegCloseReadBatchEx` | `0x728A0` | 290 | UnwindData |  |
| 158 | `ClusterRegCreateBatchNotifyPort` | `0x729D0` | 148 | UnwindData |  |
| 171 | `ClusterRegGetBatchNotification` | `0x72A70` | 240 | UnwindData |  |
| 78 | `ClusterFreeMrrResponse` | `0x74190` | 145 | UnwindData |  |
| 212 | `ClusterSendReceiveMrr` | `0x74230` | 228 | UnwindData |  |
| 213 | `ClusterSendReceiveMrrAsUser` | `0x74320` | 228 | UnwindData |  |
| 220 | `ClusterStmFindDisk` | `0x74410` | 187 | UnwindData |  |
| 371 | `RepairClusterNameAccount` | `0x7B620` | 6,750 | UnwindData |  |
| 1 | `CCHlpAddNodeUpdateCluster` | `0x7D4B0` | 287 | UnwindData |  |
| 2 | `CCHlpConfigureNode` | `0x7D810` | 1,071 | UnwindData |  |
| 3 | `CCHlpCreateClusterNameCOIfNotExists` | `0x7DC50` | 3,675 | UnwindData |  |
| 4 | `CCHlpCreateClusterNameInAD` | `0x7EAC0` | 1,231 | UnwindData |  |
| 5 | `CCHlpGetClusterServiceSecret` | `0x7EFA0` | 222 | UnwindData |  |
| 6 | `CCHlpGetDNSHostLabel` | `0x7F090` | 390 | UnwindData |  |
| 7 | `CCHlpRestoreClusterVirtualObjectToInitialState` | `0x7F220` | 207 | UnwindData |  |
| 64 | `ClusterCreateClusterStorageEnclosure` | `0x7F4C0` | 1,816 | UnwindData |  |
| 80 | `ClusterGetClusterStorageEnclosureObject` | `0x7FBE0` | 8,892 | UnwindData |  |
| 81 | `ClusterGetClusterStorageEnclosureObjects` | `0x81EB0` | 5,254 | UnwindData |  |
| 82 | `ClusterGetDriveInfo` | `0x83340` | 818 | UnwindData |  |
| 186 | `ClusterRemoveClusterStorageEnclosure` | `0x83680` | 441 | UnwindData |  |
| 215 | `ClusterSetClusterStorageEnclosure` | `0x83840` | 1,512 | UnwindData |  |
| 274 | `FreeClusStorageEnclosureInfo` | `0x83E30` | 244 | UnwindData |  |
| 275 | `FreeClusStorageEnclosureInfoArray` | `0x83F30` | 99 | UnwindData |  |
| 315 | `InitializeClusStorageEnclosureInfo` | `0x83FA0` | 35 | UnwindData |  |
| 308 | `InitializeClusFaultDomainInfoArray` | `0x83FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `InitializeClusKeyValueEntryArray` | `0x83FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `InitializeClusKeyValueStoreInfoArray` | `0x83FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `InitializeClusKeyValueStoreManagerInfo` | `0x83FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `InitializeClusKeyValueStoreManagerInfoArray` | `0x83FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `InitializeClusStorageEnclosureInfoArray` | `0x83FD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ClusterCreateFaultDomain` | `0x83FF0` | 950 | UnwindData |  |
| 66 | `ClusterCreateFaultDomainFromXML` | `0x843B0` | 447 | UnwindData |  |
| 85 | `ClusterGetFaultDomainObject` | `0x84580` | 3,927 | UnwindData |  |
| 86 | `ClusterGetFaultDomainObjects` | `0x854E0` | 2,920 | UnwindData |  |
| 87 | `ClusterGetFaultDomainState` | `0x86050` | 314 | UnwindData |  |
| 88 | `ClusterGetFaultDomainXML` | `0x86190` | 1,144 | UnwindData |  |
| 187 | `ClusterRemoveFaultDomain` | `0x86610` | 441 | UnwindData |  |
| 216 | `ClusterSetFaultDomain` | `0x867D0` | 947 | UnwindData |  |
| 217 | `ClusterSetNodeFaultDomain` | `0x86B90` | 408 | UnwindData |  |
| 265 | `FreeClusFaultDomainInfo` | `0x86D30` | 132 | UnwindData |  |
| 266 | `FreeClusFaultDomainInfoArray` | `0x86DC0` | 96 | UnwindData |  |
| 267 | `FreeClusFaultDomainXML` | `0x86E30` | 24 | UnwindData |  |
| 307 | `InitializeClusFaultDomainInfo` | `0x86E50` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `ClusterChangeVMSettings` | `0x879B0` | 1,408 | UnwindData |  |
| 69 | `ClusterCreateVMReservation` | `0x87F40` | 70 | UnwindData |  |
| 70 | `ClusterCreateVMReservationEx` | `0x87F90` | 70 | UnwindData |  |
| 71 | `ClusterCreateVMReservationWithDomains` | `0x87FE0` | 92 | UnwindData |  |
| 72 | `ClusterCreateVMReservationWithDomainsEx` | `0x88050` | 92 | UnwindData |  |
| 79 | `ClusterFreeVMReservation` | `0x880C0` | 556 | UnwindData |  |
| 92 | `ClusterGetPlacementScore` | `0x88300` | 102 | UnwindData |  |
| 93 | `ClusterGetPlacementScoreEx` | `0x88370` | 1,927 | UnwindData |  |
| 12 | `AddClusterGroupSetDependency` | `0x8B180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `AddClusterGroupSetDependencyEx` | `0x8B190` | 207 | UnwindData |  |
| 14 | `AddClusterGroupToGroupSetDependency` | `0x8B270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AddClusterGroupToGroupSetDependencyEx` | `0x8B280` | 217 | UnwindData |  |
| 35 | `CloseClusterGroupSet` | `0x8B360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ClusterAddGroupToGroupSet` | `0x8B370` | 226 | UnwindData |  |
| 52 | `ClusterAddGroupToGroupSetWithDomains` | `0x8B460` | 21 | UnwindData |  |
| 53 | `ClusterAddGroupToGroupSetWithDomainsEx` | `0x8B480` | 261 | UnwindData |  |
| 189 | `ClusterRemoveGroupFromGroupSet` | `0x8B590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `ClusterRemoveGroupFromGroupSetEx` | `0x8B5A0` | 169 | UnwindData |  |
| 232 | `CreateClusterAvailabilitySet` | `0x8B650` | 698 | UnwindData |  |
| 235 | `CreateClusterGroupSet` | `0x8B910` | 557 | UnwindData |  |
| 247 | `DeleteClusterGroupSet` | `0x8BB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `DeleteClusterGroupSetEx` | `0x8BB60` | 169 | UnwindData |  |
| 339 | `OpenClusterGroupSet` | `0x8BC10` | 447 | UnwindData |  |
| 359 | `RemoveClusterGroupSetDependency` | `0x8BDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `RemoveClusterGroupSetDependencyEx` | `0x8BDF0` | 217 | UnwindData |  |
| 361 | `RemoveClusterGroupToGroupSetDependency` | `0x8BED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `RemoveClusterGroupToGroupSetDependencyEx` | `0x8BEE0` | 217 | UnwindData |  |
| 382 | `SetClusterGroupSetDependencyExpression` | `0x8BFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `SetClusterGroupSetDependencyExpressionEx` | `0x8BFD0` | 197 | UnwindData |  |
| 23 | `AddCrossClusterGroupSetDependency` | `0x8C540` | 751 | UnwindData |  |
| 369 | `RemoveCrossClusterGroupSetDependency` | `0x8C840` | 876 | UnwindData |  |
| 50 | `ClusterAddGroupToAffinityRule` | `0x8CBC0` | 481 | UnwindData |  |
| 54 | `ClusterAffinityRuleControl` | `0x8CDB0` | 533 | UnwindData |  |
| 63 | `ClusterCreateAffinityRule` | `0x8CFD0` | 392 | UnwindData |  |
| 185 | `ClusterRemoveAffinityRule` | `0x8D160` | 290 | UnwindData |  |
| 188 | `ClusterRemoveGroupFromAffinityRule` | `0x8D290` | 481 | UnwindData |  |
| 41 | `CloseKeyValueStore` | `0x8FC30` | 214 | UnwindData |  |
| 55 | `ClusterBackupKeyValueStore` | `0x8FD10` | 688 | UnwindData |  |
| 67 | `ClusterCreateKeyValueStore` | `0x8FFD0` | 662 | UnwindData |  |
| 68 | `ClusterCreateKeyValueStoreManager` | `0x90270` | 568 | UnwindData |  |
| 73 | `ClusterDeleteKeyValueStore` | `0x904B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ClusterDeleteKeyValueStoreManager` | `0x904C0` | 441 | UnwindData |  |
| 89 | `ClusterGetKeyValueStoreManagers` | `0x90680` | 1,531 | UnwindData |  |
| 90 | `ClusterGetKeyValueStores` | `0x90C90` | 1,730 | UnwindData |  |
| 111 | `ClusterKeyValueCloseBatch` | `0x91360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ClusterKeyValueCloseBatchEx` | `0x91370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `ClusterKeyValueStoreCreateKey` | `0x91380` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `ClusterKeyValueStoreDeleteKey` | `0x913A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `ClusterKeyValueStoreQuery` | `0x913B0` | 130 | UnwindData |  |
| 117 | `ClusterKeyValueStoreQuery2` | `0x91440` | 141 | UnwindData |  |
| 118 | `ClusterKeyValueStoreUpdateKey` | `0x914E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `ClusterRestoreKeyValueStore` | `0x914F0` | 688 | UnwindData |  |
| 268 | `FreeClusKeyValueEntry` | `0x917B0` | 84 | UnwindData |  |
| 269 | `FreeClusKeyValueEntryArray` | `0x91810` | 96 | UnwindData |  |
| 270 | `FreeClusKeyValueStoreInfo` | `0x91880` | 68 | UnwindData |  |
| 271 | `FreeClusKeyValueStoreInfoArray` | `0x918D0` | 100 | UnwindData |  |
| 272 | `FreeClusKeyValueStoreManagerInfo` | `0x91940` | 68 | UnwindData |  |
| 273 | `FreeClusKeyValueStoreManagerInfoArray` | `0x91990` | 96 | UnwindData |  |
| 309 | `InitializeClusKeyValueEntry` | `0x91A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `InitializeClusKeyValueStoreInfo` | `0x91A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `OpenKeyValueStore` | `0x91A40` | 94 | UnwindData |  |
| 9 | `AddClusterFabricControllerManager` | `0x93660` | 353 | UnwindData |  |
| 356 | `RemoveClusterFabricControllerManager` | `0x937D0` | 353 | UnwindData |  |
| 317 | `InvokeClusterNativeUpdateControl` | `0x95100` | 188 | UnwindData |  |
| 110 | `ClusterKeyValueBatchAddCommand` | `0xAD230` | 134 | UnwindData |  |
| 113 | `ClusterKeyValueCreateBatch` | `0xAD2C0` | 169 | UnwindData |  |
| 147 | `ClusterRegBatchAddCommand` | `0xAD720` | 202 | UnwindData |  |
| 156 | `ClusterRegCloseReadBatchReply` | `0xAD7F0` | 63 | UnwindData |  |
| 157 | `ClusterRegCreateBatch` | `0xAD840` | 87 | UnwindData |  |
| 162 | `ClusterRegCreateReadBatch` | `0xAD8A0` | 84 | UnwindData |  |
| 177 | `ClusterRegReadBatchAddCommand` | `0xAD900` | 224 | UnwindData |  |
| 178 | `ClusterRegReadBatchReplyNextCommand` | `0xAD9F0` | 119 | UnwindData |  |
| 42 | `CluFreeFaultDomainInfo` | `0xADFF0` | 117 | UnwindData |  |
| 43 | `CluFreeGuidArrayPtr` | `0xAE070` | 50 | UnwindData |  |
| 44 | `CluFreeStr` | `0xAE0B0` | 28 | UnwindData |  |
| 45 | `CluGetDriveInfo` | `0xAE0E0` | 229 | UnwindData |  |
| 46 | `CluGetFaultDomainObject` | `0xAE1D0` | 200 | UnwindData |  |
| 47 | `CluGetFaultDomainObjects` | `0xAE2A0` | 300 | UnwindData |  |
| 48 | `CluRemoveFaultDomainObject` | `0xAE3E0` | 167 | UnwindData |  |
