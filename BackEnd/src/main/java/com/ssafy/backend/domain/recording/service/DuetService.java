package com.ssafy.backend.domain.recording.service;

import com.ssafy.backend.domain.recording.dto.DuetCreateRequestDto;
import com.ssafy.backend.domain.recording.dto.DuetFinishedListResponseDto;
import com.ssafy.backend.domain.recording.dto.DuetListResponseDto;
import com.ssafy.backend.domain.recording.dto.DuetParticipateReqeustDto;

import java.util.List;

public interface DuetService {

    // duet recording upload
    void createDuet(Long memberId, Long songId, DuetCreateRequestDto duetCreateRequestDto);
    // duet 참여하기
    void participateDuet(Long memberId, Long songId, DuetParticipateReqeustDto duetParticipateReqeustDto);
    // 완성안된 모든 duet 조회
    List<DuetListResponseDto> getAllDuetList();
    // 완성안된 내 duet list 조회
    List<DuetListResponseDto> getMyDuetList(Long memberId);

    List<DuetFinishedListResponseDto> getMyDuetFinishedList(Long memberId);

    //단일 조회
    DuetFinishedListResponseDto getDuet(Long duetId);
}
