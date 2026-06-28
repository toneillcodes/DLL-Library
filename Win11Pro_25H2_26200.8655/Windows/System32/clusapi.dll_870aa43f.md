# Binary Specification: clusapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\clusapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `870aa43f1966e8862335039aae7a7e52a3419420e3f9e6041089afb7cb5146b3`
* **Total Exported Functions:** 396

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 27 | `BackupClusterDatabase` | `0x2AEB0` | 28 | UnwindData |  |
| 388 | `SetClusterNetworkPriorityOrder` | `0x2AEB0` | 28 | UnwindData |  |
| 33 | `CloseCluster` | `0x2AEE0` | 514 | UnwindData |  |
| 49 | `ClusapiSetReasonHandler` | `0x2B0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ClusterCaptureLiveDump` | `0x2B110` | 162 | UnwindData |  |
| 57 | `ClusterCaptureLiveDumpEx` | `0x2B1C0` | 610 | UnwindData |  |
| 59 | `ClusterCloseEnum` | `0x2B430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `ClusterCloseEnumEx` | `0x2B440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `ClusterEnum` | `0x2B450` | 182 | UnwindData |  |
| 76 | `ClusterEnumEx` | `0x2B510` | 88 | UnwindData |  |
| 83 | `ClusterGetEnumCount` | `0x2B570` | 35 | UnwindData |  |
| 84 | `ClusterGetEnumCountEx` | `0x2B5A0` | 40 | UnwindData |  |
| 91 | `ClusterGetMaximumAccessForToken` | `0x2B5D0` | 140 | UnwindData |  |
| 94 | `ClusterGroupCloseEnum` | `0x2B670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `ClusterGroupCloseEnumEx` | `0x2B680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `ClusterGroupEnum` | `0x2B690` | 182 | UnwindData |  |
| 99 | `ClusterGroupEnumEx` | `0x2B750` | 558 | UnwindData |  |
| 100 | `ClusterGroupGetEnumCount` | `0x2B990` | 35 | UnwindData |  |
| 101 | `ClusterGroupGetEnumCountEx` | `0x2B9C0` | 35 | UnwindData |  |
| 102 | `ClusterGroupOpenEnum` | `0x2B9F0` | 189 | UnwindData |  |
| 103 | `ClusterGroupOpenEnumEx` | `0x2BAC0` | 257 | UnwindData |  |
| 104 | `ClusterGroupSetCloseEnum` | `0x2BBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `ClusterGroupSetEnum` | `0x2BBE0` | 163 | UnwindData |  |
| 108 | `ClusterGroupSetGetEnumCount` | `0x2BC90` | 35 | UnwindData |  |
| 109 | `ClusterGroupSetOpenEnum` | `0x2BCC0` | 162 | UnwindData |  |
| 119 | `ClusterNetInterfaceCloseEnum` | `0x2BD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `ClusterNetInterfaceEnum` | `0x2BD80` | 176 | UnwindData |  |
| 123 | `ClusterNetInterfaceOpenEnum` | `0x2BE40` | 225 | UnwindData |  |
| 129 | `ClusterNetworkHealthFreeInterfaceConnections` | `0x2BF30` | 98 | UnwindData |  |
| 130 | `ClusterNetworkHealthFreeNodeConnections` | `0x2BF30` | 98 | UnwindData |  |
| 131 | `ClusterNetworkHealthGetInterfaceConnections` | `0x2BFA0` | 613 | UnwindData |  |
| 132 | `ClusterNetworkHealthGetNodeConnections` | `0x2C210` | 1,415 | UnwindData |  |
| 134 | `ClusterNodeCloseEnum` | `0x2C7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `ClusterNodeCloseEnumEx` | `0x2C7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `ClusterNodeEnum` | `0x2C7C0` | 182 | UnwindData |  |
| 139 | `ClusterNodeEnumEx` | `0x2C880` | 88 | UnwindData |  |
| 140 | `ClusterNodeGetEnumCount` | `0x2C8E0` | 35 | UnwindData |  |
| 141 | `ClusterNodeGetEnumCountEx` | `0x2C910` | 40 | UnwindData |  |
| 142 | `ClusterNodeOpenEnum` | `0x2C940` | 202 | UnwindData |  |
| 143 | `ClusterNodeOpenEnumEx` | `0x2CA10` | 220 | UnwindData |  |
| 145 | `ClusterOpenEnum` | `0x2CB00` | 258 | UnwindData |  |
| 146 | `ClusterOpenEnumEx` | `0x2CC10` | 300 | UnwindData |  |
| 192 | `ClusterResourceCloseEnumEx` | `0x2CD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 198 | `ClusterResourceEnumEx` | `0x2CD60` | 600 | UnwindData |  |
| 200 | `ClusterResourceGetEnumCountEx` | `0x2CFC0` | 35 | UnwindData |  |
| 202 | `ClusterResourceOpenEnumEx` | `0x2CFF0` | 265 | UnwindData |  |
| 214 | `ClusterSetAccountAccess` | `0x2D100` | 1,152 | UnwindData |  |
| 218 | `ClusterSharedVolumeClearBackupState` | `0x2D590` | 45 | UnwindData |  |
| 219 | `ClusterSharedVolumeSetSnapshotState` | `0x2D5D0` | 348 | UnwindData |  |
| 221 | `ClusterUpgradeFunctionalLevel` | `0x2D740` | 1,191 | UnwindData |  |
| 222 | `ClusterUpgradeFunctionalLevelEx` | `0x2DBF0` | 1,141 | UnwindData |  |
| 223 | `ClusterWprAddMarker` | `0x2E070` | 283 | UnwindData |  |
| 224 | `ClusterWprCancel` | `0x2E1A0` | 253 | UnwindData |  |
| 225 | `ClusterWprCaptureState` | `0x2E2B0` | 283 | UnwindData |  |
| 226 | `ClusterWprFlush` | `0x2E3E0` | 283 | UnwindData |  |
| 227 | `ClusterWprFlush2` | `0x2E510` | 324 | UnwindData |  |
| 228 | `ClusterWprStart` | `0x2E660` | 342 | UnwindData |  |
| 229 | `ClusterWprStop` | `0x2E7C0` | 283 | UnwindData |  |
| 230 | `ClusterWprStop2` | `0x2E8F0` | 324 | UnwindData |  |
| 283 | `GetClusterInformation` | `0x2EB30` | 645 | UnwindData |  |
| 296 | `GetClusterQuorumResource` | `0x2EDC0` | 407 | UnwindData |  |
| 302 | `GetClusterSharedVolumeNameForFile` | `0x2EF60` | 815 | UnwindData |  |
| 305 | `GetNodeClusterState` | `0x2F2A0` | 219 | UnwindData |  |
| 318 | `IsFileOnClusterSharedVolume` | `0x2F390` | 346 | UnwindData |  |
| 334 | `OpenCluster` | `0x2F4F0` | 34 | UnwindData |  |
| 335 | `OpenClusterEx` | `0x2F520` | 33 | UnwindData |  |
| 336 | `OpenClusterEx2` | `0x2F550` | 27 | UnwindData |  |
| 374 | `RestoreClusterDatabase` | `0x2F580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 394 | `SetClusterServiceAccountPassword` | `0x2F580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 384 | `SetClusterName` | `0x2F590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `SetClusterNameEx` | `0x2F5A0` | 523 | UnwindData |  |
| 389 | `SetClusterQuorumResource` | `0x2F7C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 390 | `SetClusterQuorumResourceEx` | `0x2F7D0` | 226 | UnwindData |  |
| 22 | `AddClusterStorageNode` | `0x38D40` | 11,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 368 | `RemoveClusterStorageNode` | `0x38D40` | 11,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetClusterUserMgrResource` | `0x3B870` | 277 | UnwindData |  |
| 16 | `AddClusterNode` | `0x41E70` | 26 | UnwindData |  |
| 17 | `AddClusterNodeEx` | `0x41E90` | 5,474 | UnwindData |  |
| 144 | `ClusterNodeReplacement` | `0x43400` | 435 | UnwindData |  |
| 231 | `CreateCluster` | `0x435C0` | 49 | UnwindData |  |
| 236 | `CreateClusterManagementPoint` | `0x43600` | 260 | UnwindData |  |
| 237 | `CreateClusterNameAccount` | `0x43710` | 8,982 | UnwindData |  |
| 253 | `DestroyCluster` | `0x45A30` | 3,441 | UnwindData |  |
| 256 | `DetermineCNOResTypeFromCluster` | `0x467B0` | 105 | UnwindData |  |
| 257 | `DetermineCNOResTypeFromNodelist` | `0x46820` | 107 | UnwindData |  |
| 258 | `DetermineClusterCloudTypeFromCluster` | `0x468A0` | 189 | UnwindData |  |
| 259 | `DetermineClusterCloudTypeFromNodelist` | `0x46970` | 184 | UnwindData |  |
| 303 | `GetClusterUserMgrCredential` | `0x46A30` | 1,972 | UnwindData |  |
| 304 | `GetNodeCloudTypeDW` | `0x471F0` | 82 | UnwindData |  |
| 363 | `RemoveClusterNameAccount` | `0x47250` | 2,300 | UnwindData |  |
| 10 | `AddClusterGroupDependency` | `0x4D5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `AddClusterGroupDependencyEx` | `0x4D5C0` | 217 | UnwindData |  |
| 29 | `CancelClusterGroupOperation` | `0x4D6A0` | 85 | UnwindData |  |
| 34 | `CloseClusterGroup` | `0x4D700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `CreateClusterGroup` | `0x4D710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `CreateClusterGroupEx` | `0x4D720` | 618 | UnwindData |  |
| 245 | `DeleteClusterGroup` | `0x4D990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `DeleteClusterGroupEx` | `0x4D9A0` | 186 | UnwindData |  |
| 254 | `DestroyClusterGroup` | `0x4DA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `DestroyClusterGroupEx` | `0x4DA70` | 192 | UnwindData |  |
| 276 | `GetClusterFromGroup` | `0x4DB40` | 94 | UnwindData |  |
| 282 | `GetClusterGroupState` | `0x4DBB0` | 317 | UnwindData |  |
| 319 | `MoveClusterGroup` | `0x4DD00` | 32 | UnwindData |  |
| 320 | `MoveClusterGroupEx` | `0x4DD30` | 29 | UnwindData |  |
| 321 | `MoveClusterGroupEx2` | `0x4DD60` | 746 | UnwindData |  |
| 322 | `OfflineClusterGroup` | `0x4E050` | 29 | UnwindData |  |
| 323 | `OfflineClusterGroupEx` | `0x4E080` | 21 | UnwindData |  |
| 324 | `OfflineClusterGroupEx2` | `0x4E0A0` | 251 | UnwindData |  |
| 328 | `OnlineClusterGroup` | `0x4E1B0` | 374 | UnwindData |  |
| 329 | `OnlineClusterGroupEx` | `0x4E330` | 29 | UnwindData |  |
| 330 | `OnlineClusterGroupEx2` | `0x4E360` | 516 | UnwindData |  |
| 337 | `OpenClusterGroup` | `0x4E570` | 32 | UnwindData |  |
| 338 | `OpenClusterGroupEx` | `0x4E5A0` | 31 | UnwindData |  |
| 357 | `RemoveClusterGroupDependency` | `0x4E5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `RemoveClusterGroupDependencyEx` | `0x4E5E0` | 217 | UnwindData |  |
| 378 | `SetClusterGroupName` | `0x4E6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 379 | `SetClusterGroupNameEx` | `0x4E6D0` | 197 | UnwindData |  |
| 380 | `SetClusterGroupNodeList` | `0x4E7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `SetClusterGroupNodeListEx` | `0x4E7B0` | 694 | UnwindData |  |
| 395 | `SetGroupDependencyExpression` | `0x4EA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 396 | `SetGroupDependencyExpressionEx` | `0x4EA80` | 197 | UnwindData |  |
| 36 | `CloseClusterNetInterface` | `0x4F8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `GetClusterFromNetInterface` | `0x4F900` | 84 | UnwindData |  |
| 285 | `GetClusterNetInterface` | `0x4F960` | 285 | UnwindData |  |
| 287 | `GetClusterNetInterfaceState` | `0x4FA90` | 112 | UnwindData |  |
| 340 | `OpenClusterNetInterface` | `0x4FB10` | 32 | UnwindData |  |
| 341 | `OpenClusterNetInterfaceEx` | `0x4FB40` | 31 | UnwindData |  |
| 61 | `ClusterControl` | `0x55FC0` | 69 | UnwindData |  |
| 62 | `ClusterControlEx` | `0x56010` | 609 | UnwindData |  |
| 96 | `ClusterGroupControl` | `0x56280` | 69 | UnwindData |  |
| 97 | `ClusterGroupControlEx` | `0x562D0` | 572 | UnwindData |  |
| 105 | `ClusterGroupSetControl` | `0x56520` | 69 | UnwindData |  |
| 106 | `ClusterGroupSetControlEx` | `0x56570` | 560 | UnwindData |  |
| 120 | `ClusterNetInterfaceControl` | `0x567B0` | 69 | UnwindData |  |
| 121 | `ClusterNetInterfaceControlEx` | `0x56800` | 572 | UnwindData |  |
| 125 | `ClusterNetworkControl` | `0x56A50` | 69 | UnwindData |  |
| 126 | `ClusterNetworkControlEx` | `0x56AA0` | 572 | UnwindData |  |
| 136 | `ClusterNodeControl` | `0x56CF0` | 69 | UnwindData |  |
| 137 | `ClusterNodeControlEx` | `0x56D40` | 676 | UnwindData |  |
| 193 | `ClusterResourceControl` | `0x56FF0` | 74 | UnwindData |  |
| 194 | `ClusterResourceControlAsUser` | `0x57040` | 69 | UnwindData |  |
| 195 | `ClusterResourceControlAsUserEx` | `0x57090` | 97 | UnwindData |  |
| 196 | `ClusterResourceControlEx` | `0x57100` | 81 | UnwindData |  |
| 204 | `ClusterResourceTypeControl` | `0x57160` | 86 | UnwindData |  |
| 205 | `ClusterResourceTypeControlAsUser` | `0x571C0` | 86 | UnwindData |  |
| 206 | `ClusterResourceTypeControlAsUserEx` | `0x57220` | 93 | UnwindData |  |
| 207 | `ClusterResourceTypeControlEx` | `0x57290` | 93 | UnwindData |  |
| 37 | `CloseClusterNetwork` | `0x58750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `ClusterNetworkCloseEnum` | `0x58760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `ClusterNetworkEnum` | `0x58770` | 182 | UnwindData |  |
| 128 | `ClusterNetworkGetEnumCount` | `0x58830` | 35 | UnwindData |  |
| 133 | `ClusterNetworkOpenEnum` | `0x58860` | 189 | UnwindData |  |
| 278 | `GetClusterFromNetwork` | `0x58930` | 81 | UnwindData |  |
| 288 | `GetClusterNetworkId` | `0x58990` | 205 | UnwindData |  |
| 290 | `GetClusterNetworkState` | `0x58A70` | 112 | UnwindData |  |
| 342 | `OpenClusterNetwork` | `0x58AF0` | 32 | UnwindData |  |
| 343 | `OpenClusterNetworkEx` | `0x58B20` | 31 | UnwindData |  |
| 386 | `SetClusterNetworkName` | `0x58B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 387 | `SetClusterNetworkNameEx` | `0x58B60` | 197 | UnwindData |  |
| 38 | `CloseClusterNode` | `0x5AD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `EvictClusterNode` | `0x5AD40` | 33 | UnwindData |  |
| 261 | `EvictClusterNodeEx` | `0x5AD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `EvictClusterNodeEx2` | `0x5AD80` | 1,181 | UnwindData |  |
| 279 | `GetClusterFromNode` | `0x5B230` | 84 | UnwindData |  |
| 291 | `GetClusterNodeId` | `0x5B290` | 229 | UnwindData |  |
| 293 | `GetClusterNodeState` | `0x5B380` | 128 | UnwindData |  |
| 344 | `OpenClusterNode` | `0x5B410` | 32 | UnwindData |  |
| 345 | `OpenClusterNodeById` | `0x5B440` | 1,440 | UnwindData |  |
| 346 | `OpenClusterNodeEx` | `0x5B9F0` | 31 | UnwindData |  |
| 350 | `PauseClusterNode` | `0x5BA20` | 29 | UnwindData |  |
| 351 | `PauseClusterNodeEx` | `0x5BA50` | 21 | UnwindData |  |
| 352 | `PauseClusterNodeEx2` | `0x5BA70` | 887 | UnwindData |  |
| 375 | `ResumeClusterNode` | `0x5BDF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `ResumeClusterNodeEx` | `0x5BE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 377 | `ResumeClusterNodeEx2` | `0x5BE20` | 597 | UnwindData |  |
| 39 | `CloseClusterNotifyPort` | `0x61570` | 122 | UnwindData |  |
| 238 | `CreateClusterNotifyPort` | `0x615F0` | 497 | UnwindData |  |
| 239 | `CreateClusterNotifyPortV2` | `0x617F0` | 694 | UnwindData |  |
| 294 | `GetClusterNotify` | `0x61AB0` | 471 | UnwindData |  |
| 295 | `GetClusterNotifyV2` | `0x61C90` | 1,055 | UnwindData |  |
| 306 | `GetNotifyEventHandle` | `0x620C0` | 167 | UnwindData |  |
| 353 | `RegisterClusterNotify` | `0x62170` | 541 | UnwindData |  |
| 354 | `RegisterClusterNotifyV2` | `0x623A0` | 104 | UnwindData |  |
| 355 | `RegisterClusterResourceTypeNotifyV2` | `0x62410` | 100 | UnwindData |  |
| 77 | `ClusterFreeMemory` | `0x670A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `ClusterRegCloseKey` | `0x670C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `ClusterRegCreateKey` | `0x670D0` | 53 | UnwindData |  |
| 160 | `ClusterRegCreateKeyEx` | `0x67110` | 804 | UnwindData |  |
| 161 | `ClusterRegCreateKeyForceSync` | `0x67440` | 123 | UnwindData |  |
| 163 | `ClusterRegDeleteKey` | `0x674D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 164 | `ClusterRegDeleteKeyEx` | `0x674E0` | 197 | UnwindData |  |
| 165 | `ClusterRegDeleteKeyForceSync` | `0x675B0` | 76 | UnwindData |  |
| 166 | `ClusterRegDeleteValue` | `0x67610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `ClusterRegDeleteValueEx` | `0x67620` | 197 | UnwindData |  |
| 168 | `ClusterRegDeleteValueForceSync` | `0x676F0` | 76 | UnwindData |  |
| 169 | `ClusterRegEnumKey` | `0x67750` | 238 | UnwindData |  |
| 170 | `ClusterRegEnumValue` | `0x67850` | 355 | UnwindData |  |
| 172 | `ClusterRegGetKeySecurity` | `0x679C0` | 143 | UnwindData |  |
| 173 | `ClusterRegOpenKey` | `0x67A60` | 494 | UnwindData |  |
| 174 | `ClusterRegQueryAllValues` | `0x67C60` | 105 | UnwindData |  |
| 175 | `ClusterRegQueryInfoKey` | `0x67CD0` | 308 | UnwindData |  |
| 176 | `ClusterRegQueryValue` | `0x67E10` | 224 | UnwindData |  |
| 179 | `ClusterRegSetKeySecurity` | `0x67F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `ClusterRegSetKeySecurityEx` | `0x67F10` | 267 | UnwindData |  |
| 181 | `ClusterRegSetValue` | `0x68030` | 29 | UnwindData |  |
| 182 | `ClusterRegSetValueEx` | `0x68060` | 232 | UnwindData |  |
| 183 | `ClusterRegSetValueForceSync` | `0x68150` | 105 | UnwindData |  |
| 184 | `ClusterRegSyncDatabase` | `0x681C0` | 84 | UnwindData |  |
| 281 | `GetClusterGroupKey` | `0x68220` | 221 | UnwindData |  |
| 284 | `GetClusterKey` | `0x68310` | 344 | UnwindData |  |
| 286 | `GetClusterNetInterfaceKey` | `0x68470` | 221 | UnwindData |  |
| 289 | `GetClusterNetworkKey` | `0x68560` | 222 | UnwindData |  |
| 292 | `GetClusterNodeKey` | `0x68650` | 284 | UnwindData |  |
| 298 | `GetClusterResourceKey` | `0x68780` | 221 | UnwindData |  |
| 301 | `GetClusterResourceTypeKey` | `0x68870` | 26,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `AddClusterResourceDependency` | `0x6EE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `AddClusterResourceDependencyEx` | `0x6EE30` | 242 | UnwindData |  |
| 20 | `AddClusterResourceNode` | `0x6EF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `AddClusterResourceNodeEx` | `0x6EF40` | 301 | UnwindData |  |
| 24 | `AddResourceToClusterSharedVolumes` | `0x6F080` | 90 | UnwindData |  |
| 25 | `AddResourceToClusterSharedVolumesEx` | `0x6F0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `AddResourceToClusterSharedVolumesEx2` | `0x6F0F0` | 252 | UnwindData |  |
| 28 | `CanResourceBeDependent` | `0x6F200` | 139 | UnwindData |  |
| 30 | `ChangeClusterResourceGroup` | `0x6F2A0` | 120 | UnwindData |  |
| 31 | `ChangeClusterResourceGroupEx` | `0x6F320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ChangeClusterResourceGroupEx2` | `0x6F330` | 324 | UnwindData |  |
| 40 | `CloseClusterResource` | `0x6F480` | 549 | UnwindData |  |
| 191 | `ClusterResourceCloseEnum` | `0x6F6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 197 | `ClusterResourceEnum` | `0x6F6C0` | 189 | UnwindData |  |
| 199 | `ClusterResourceGetEnumCount` | `0x6F790` | 49 | UnwindData |  |
| 201 | `ClusterResourceOpenEnum` | `0x6F7D0` | 189 | UnwindData |  |
| 203 | `ClusterResourceTypeCloseEnum` | `0x6F8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `ClusterResourceTypeEnum` | `0x6F8B0` | 206 | UnwindData |  |
| 209 | `ClusterResourceTypeGetEnumCount` | `0x6F990` | 49 | UnwindData |  |
| 210 | `ClusterResourceTypeOpenEnum` | `0x6F9D0` | 213 | UnwindData |  |
| 240 | `CreateClusterResource` | `0x6FAB0` | 21 | UnwindData |  |
| 241 | `CreateClusterResourceEx` | `0x6FAD0` | 406 | UnwindData |  |
| 242 | `CreateClusterResourceType` | `0x6FC70` | 37 | UnwindData |  |
| 243 | `CreateClusterResourceTypeEx` | `0x6FCA0` | 295 | UnwindData |  |
| 244 | `CreateClusterResourceWithId` | `0x6FDD0` | 23 | UnwindData |  |
| 249 | `DeleteClusterResource` | `0x6FFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `DeleteClusterResourceEx` | `0x6FFB0` | 157 | UnwindData |  |
| 251 | `DeleteClusterResourceType` | `0x70060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `DeleteClusterResourceTypeEx` | `0x70070` | 248 | UnwindData |  |
| 263 | `FailClusterResource` | `0x70170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `FailClusterResourceEx` | `0x70180` | 185 | UnwindData |  |
| 280 | `GetClusterFromResource` | `0x70240` | 94 | UnwindData |  |
| 297 | `GetClusterResourceDependencyExpression` | `0x702B0` | 260 | UnwindData |  |
| 299 | `GetClusterResourceNetworkName` | `0x703C0` | 293 | UnwindData |  |
| 300 | `GetClusterResourceState` | `0x704F0` | 406 | UnwindData |  |
| 325 | `OfflineClusterResource` | `0x70690` | 82 | UnwindData |  |
| 326 | `OfflineClusterResourceEx` | `0x706F0` | 21 | UnwindData |  |
| 327 | `OfflineClusterResourceEx2` | `0x70710` | 263 | UnwindData |  |
| 331 | `OnlineClusterResource` | `0x70820` | 82 | UnwindData |  |
| 332 | `OnlineClusterResourceEx` | `0x70880` | 21 | UnwindData |  |
| 333 | `OnlineClusterResourceEx2` | `0x708A0` | 263 | UnwindData |  |
| 347 | `OpenClusterResource` | `0x709B0` | 32 | UnwindData |  |
| 348 | `OpenClusterResourceEx` | `0x709E0` | 31 | UnwindData |  |
| 364 | `RemoveClusterResourceDependency` | `0x70A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `RemoveClusterResourceDependencyEx` | `0x70A20` | 242 | UnwindData |  |
| 366 | `RemoveClusterResourceNode` | `0x70B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | `RemoveClusterResourceNodeEx` | `0x70B30` | 301 | UnwindData |  |
| 370 | `RemoveResourceFromClusterSharedVolumes` | `0x70C70` | 87 | UnwindData |  |
| 372 | `RestartClusterResource` | `0x70CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `RestartClusterResourceEx` | `0x70CE0` | 208 | UnwindData |  |
| 391 | `SetClusterResourceDependencyExpression` | `0x70DC0` | 99 | UnwindData |  |
| 392 | `SetClusterResourceName` | `0x70E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `SetClusterResourceNameEx` | `0x70E40` | 213 | UnwindData |  |
| 148 | `ClusterRegBatchCloseNotification` | `0x71C10` | 135 | UnwindData |  |
| 149 | `ClusterRegBatchReadCommand` | `0x71CA0` | 98 | UnwindData |  |
| 150 | `ClusterRegCloseBatch` | `0x71D10` | 266 | UnwindData |  |
| 151 | `ClusterRegCloseBatchEx` | `0x71E20` | 99 | UnwindData |  |
| 152 | `ClusterRegCloseBatchNotifyPort` | `0x71E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `ClusterRegCloseReadBatch` | `0x71EA0` | 282 | UnwindData |  |
| 155 | `ClusterRegCloseReadBatchEx` | `0x71FC0` | 290 | UnwindData |  |
| 158 | `ClusterRegCreateBatchNotifyPort` | `0x720F0` | 148 | UnwindData |  |
| 171 | `ClusterRegGetBatchNotification` | `0x72190` | 240 | UnwindData |  |
| 78 | `ClusterFreeMrrResponse` | `0x738B0` | 145 | UnwindData |  |
| 212 | `ClusterSendReceiveMrr` | `0x73950` | 228 | UnwindData |  |
| 213 | `ClusterSendReceiveMrrAsUser` | `0x73A40` | 228 | UnwindData |  |
| 220 | `ClusterStmFindDisk` | `0x73B30` | 187 | UnwindData |  |
| 371 | `RepairClusterNameAccount` | `0x7AD40` | 6,750 | UnwindData |  |
| 1 | `CCHlpAddNodeUpdateCluster` | `0x7CBD0` | 287 | UnwindData |  |
| 2 | `CCHlpConfigureNode` | `0x7CF30` | 1,071 | UnwindData |  |
| 3 | `CCHlpCreateClusterNameCOIfNotExists` | `0x7D370` | 3,675 | UnwindData |  |
| 4 | `CCHlpCreateClusterNameInAD` | `0x7E1E0` | 1,231 | UnwindData |  |
| 5 | `CCHlpGetClusterServiceSecret` | `0x7E6C0` | 222 | UnwindData |  |
| 6 | `CCHlpGetDNSHostLabel` | `0x7E7B0` | 390 | UnwindData |  |
| 7 | `CCHlpRestoreClusterVirtualObjectToInitialState` | `0x7E940` | 207 | UnwindData |  |
| 64 | `ClusterCreateClusterStorageEnclosure` | `0x7EBE0` | 1,816 | UnwindData |  |
| 80 | `ClusterGetClusterStorageEnclosureObject` | `0x7F300` | 8,892 | UnwindData |  |
| 81 | `ClusterGetClusterStorageEnclosureObjects` | `0x815D0` | 5,254 | UnwindData |  |
| 82 | `ClusterGetDriveInfo` | `0x82A60` | 818 | UnwindData |  |
| 186 | `ClusterRemoveClusterStorageEnclosure` | `0x82DA0` | 441 | UnwindData |  |
| 215 | `ClusterSetClusterStorageEnclosure` | `0x82F60` | 1,512 | UnwindData |  |
| 274 | `FreeClusStorageEnclosureInfo` | `0x83550` | 244 | UnwindData |  |
| 275 | `FreeClusStorageEnclosureInfoArray` | `0x83650` | 99 | UnwindData |  |
| 315 | `InitializeClusStorageEnclosureInfo` | `0x836C0` | 35 | UnwindData |  |
| 308 | `InitializeClusFaultDomainInfoArray` | `0x836F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `InitializeClusKeyValueEntryArray` | `0x836F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `InitializeClusKeyValueStoreInfoArray` | `0x836F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 313 | `InitializeClusKeyValueStoreManagerInfo` | `0x836F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 314 | `InitializeClusKeyValueStoreManagerInfoArray` | `0x836F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 316 | `InitializeClusStorageEnclosureInfoArray` | `0x836F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ClusterCreateFaultDomain` | `0x83710` | 950 | UnwindData |  |
| 66 | `ClusterCreateFaultDomainFromXML` | `0x83AD0` | 447 | UnwindData |  |
| 85 | `ClusterGetFaultDomainObject` | `0x83CA0` | 3,927 | UnwindData |  |
| 86 | `ClusterGetFaultDomainObjects` | `0x84C00` | 2,920 | UnwindData |  |
| 87 | `ClusterGetFaultDomainState` | `0x85770` | 314 | UnwindData |  |
| 88 | `ClusterGetFaultDomainXML` | `0x858B0` | 1,144 | UnwindData |  |
| 187 | `ClusterRemoveFaultDomain` | `0x85D30` | 441 | UnwindData |  |
| 216 | `ClusterSetFaultDomain` | `0x85EF0` | 947 | UnwindData |  |
| 217 | `ClusterSetNodeFaultDomain` | `0x862B0` | 408 | UnwindData |  |
| 265 | `FreeClusFaultDomainInfo` | `0x86450` | 132 | UnwindData |  |
| 266 | `FreeClusFaultDomainInfoArray` | `0x864E0` | 96 | UnwindData |  |
| 267 | `FreeClusFaultDomainXML` | `0x86550` | 24 | UnwindData |  |
| 307 | `InitializeClusFaultDomainInfo` | `0x86570` | 2,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `ClusterChangeVMSettings` | `0x870D0` | 1,408 | UnwindData |  |
| 69 | `ClusterCreateVMReservation` | `0x87660` | 70 | UnwindData |  |
| 70 | `ClusterCreateVMReservationEx` | `0x876B0` | 70 | UnwindData |  |
| 71 | `ClusterCreateVMReservationWithDomains` | `0x87700` | 92 | UnwindData |  |
| 72 | `ClusterCreateVMReservationWithDomainsEx` | `0x87770` | 92 | UnwindData |  |
| 79 | `ClusterFreeVMReservation` | `0x877E0` | 556 | UnwindData |  |
| 92 | `ClusterGetPlacementScore` | `0x87A20` | 102 | UnwindData |  |
| 93 | `ClusterGetPlacementScoreEx` | `0x87A90` | 1,927 | UnwindData |  |
| 12 | `AddClusterGroupSetDependency` | `0x8A8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `AddClusterGroupSetDependencyEx` | `0x8A8B0` | 207 | UnwindData |  |
| 14 | `AddClusterGroupToGroupSetDependency` | `0x8A990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AddClusterGroupToGroupSetDependencyEx` | `0x8A9A0` | 217 | UnwindData |  |
| 35 | `CloseClusterGroupSet` | `0x8AA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `ClusterAddGroupToGroupSet` | `0x8AA90` | 226 | UnwindData |  |
| 52 | `ClusterAddGroupToGroupSetWithDomains` | `0x8AB80` | 21 | UnwindData |  |
| 53 | `ClusterAddGroupToGroupSetWithDomainsEx` | `0x8ABA0` | 261 | UnwindData |  |
| 189 | `ClusterRemoveGroupFromGroupSet` | `0x8ACB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `ClusterRemoveGroupFromGroupSetEx` | `0x8ACC0` | 169 | UnwindData |  |
| 232 | `CreateClusterAvailabilitySet` | `0x8AD70` | 698 | UnwindData |  |
| 235 | `CreateClusterGroupSet` | `0x8B030` | 557 | UnwindData |  |
| 247 | `DeleteClusterGroupSet` | `0x8B270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 248 | `DeleteClusterGroupSetEx` | `0x8B280` | 169 | UnwindData |  |
| 339 | `OpenClusterGroupSet` | `0x8B330` | 447 | UnwindData |  |
| 359 | `RemoveClusterGroupSetDependency` | `0x8B500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `RemoveClusterGroupSetDependencyEx` | `0x8B510` | 217 | UnwindData |  |
| 361 | `RemoveClusterGroupToGroupSetDependency` | `0x8B5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 362 | `RemoveClusterGroupToGroupSetDependencyEx` | `0x8B600` | 217 | UnwindData |  |
| 382 | `SetClusterGroupSetDependencyExpression` | `0x8B6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `SetClusterGroupSetDependencyExpressionEx` | `0x8B6F0` | 197 | UnwindData |  |
| 23 | `AddCrossClusterGroupSetDependency` | `0x8BC60` | 751 | UnwindData |  |
| 369 | `RemoveCrossClusterGroupSetDependency` | `0x8BF60` | 876 | UnwindData |  |
| 50 | `ClusterAddGroupToAffinityRule` | `0x8C2E0` | 481 | UnwindData |  |
| 54 | `ClusterAffinityRuleControl` | `0x8C4D0` | 533 | UnwindData |  |
| 63 | `ClusterCreateAffinityRule` | `0x8C6F0` | 392 | UnwindData |  |
| 185 | `ClusterRemoveAffinityRule` | `0x8C880` | 290 | UnwindData |  |
| 188 | `ClusterRemoveGroupFromAffinityRule` | `0x8C9B0` | 481 | UnwindData |  |
| 41 | `CloseKeyValueStore` | `0x8F350` | 214 | UnwindData |  |
| 55 | `ClusterBackupKeyValueStore` | `0x8F430` | 688 | UnwindData |  |
| 67 | `ClusterCreateKeyValueStore` | `0x8F6F0` | 662 | UnwindData |  |
| 68 | `ClusterCreateKeyValueStoreManager` | `0x8F990` | 568 | UnwindData |  |
| 73 | `ClusterDeleteKeyValueStore` | `0x8FBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `ClusterDeleteKeyValueStoreManager` | `0x8FBE0` | 441 | UnwindData |  |
| 89 | `ClusterGetKeyValueStoreManagers` | `0x8FDA0` | 1,531 | UnwindData |  |
| 90 | `ClusterGetKeyValueStores` | `0x903B0` | 1,730 | UnwindData |  |
| 111 | `ClusterKeyValueCloseBatch` | `0x90A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ClusterKeyValueCloseBatchEx` | `0x90A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `ClusterKeyValueStoreCreateKey` | `0x90AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `ClusterKeyValueStoreDeleteKey` | `0x90AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `ClusterKeyValueStoreQuery` | `0x90AD0` | 130 | UnwindData |  |
| 117 | `ClusterKeyValueStoreQuery2` | `0x90B60` | 141 | UnwindData |  |
| 118 | `ClusterKeyValueStoreUpdateKey` | `0x90C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `ClusterRestoreKeyValueStore` | `0x90C10` | 688 | UnwindData |  |
| 268 | `FreeClusKeyValueEntry` | `0x90ED0` | 84 | UnwindData |  |
| 269 | `FreeClusKeyValueEntryArray` | `0x90F30` | 96 | UnwindData |  |
| 270 | `FreeClusKeyValueStoreInfo` | `0x90FA0` | 68 | UnwindData |  |
| 271 | `FreeClusKeyValueStoreInfoArray` | `0x90FF0` | 100 | UnwindData |  |
| 272 | `FreeClusKeyValueStoreManagerInfo` | `0x91060` | 68 | UnwindData |  |
| 273 | `FreeClusKeyValueStoreManagerInfoArray` | `0x910B0` | 96 | UnwindData |  |
| 309 | `InitializeClusKeyValueEntry` | `0x91120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 311 | `InitializeClusKeyValueStoreInfo` | `0x91140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `OpenKeyValueStore` | `0x91160` | 94 | UnwindData |  |
| 9 | `AddClusterFabricControllerManager` | `0x92D80` | 353 | UnwindData |  |
| 356 | `RemoveClusterFabricControllerManager` | `0x92EF0` | 353 | UnwindData |  |
| 317 | `InvokeClusterNativeUpdateControl` | `0x94820` | 188 | UnwindData |  |
| 110 | `ClusterKeyValueBatchAddCommand` | `0xAC960` | 134 | UnwindData |  |
| 113 | `ClusterKeyValueCreateBatch` | `0xAC9F0` | 169 | UnwindData |  |
| 147 | `ClusterRegBatchAddCommand` | `0xACE50` | 202 | UnwindData |  |
| 156 | `ClusterRegCloseReadBatchReply` | `0xACF20` | 63 | UnwindData |  |
| 157 | `ClusterRegCreateBatch` | `0xACF70` | 87 | UnwindData |  |
| 162 | `ClusterRegCreateReadBatch` | `0xACFD0` | 84 | UnwindData |  |
| 177 | `ClusterRegReadBatchAddCommand` | `0xAD030` | 224 | UnwindData |  |
| 178 | `ClusterRegReadBatchReplyNextCommand` | `0xAD120` | 119 | UnwindData |  |
| 42 | `CluFreeFaultDomainInfo` | `0xAD720` | 117 | UnwindData |  |
| 43 | `CluFreeGuidArrayPtr` | `0xAD7A0` | 50 | UnwindData |  |
| 44 | `CluFreeStr` | `0xAD7E0` | 28 | UnwindData |  |
| 45 | `CluGetDriveInfo` | `0xAD810` | 229 | UnwindData |  |
| 46 | `CluGetFaultDomainObject` | `0xAD900` | 200 | UnwindData |  |
| 47 | `CluGetFaultDomainObjects` | `0xAD9D0` | 300 | UnwindData |  |
| 48 | `CluRemoveFaultDomainObject` | `0xADB10` | 167 | UnwindData |  |
