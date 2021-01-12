/*
 Copyright (c) 2003-2020, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or https://ckeditor.com/legal/ckeditor-oss-license
*/
CKEDITOR.addTemplates("default", {
    imagesPath: CKEDITOR.getUrl(CKEDITOR.plugins.getPath("templates") + "templates/images/"), templates: [{ title: "동아리, 대외 활동 양식", image: "circle.png", description: "동아리/대외 활동에 관한 양식을 불러옵니다.", html: '<span style="font-size:36px;">동아리/대외 활동 소개</span><br><br><p>동아리/대외활동 이름 : </p><br><br><p>활동 기간 : </p><br><br><p>동아리/대외활동 정보 : </p><br><br><hr><br><br><span style="font-size:36px;">활동 내용</span><br><br><p>내가 맡은 역할 : </p><br><br><p>느낀 점 : </p><br><br>' }, {
        title: "교육 활동", image: "study.png", description: "교육 활동에 관한 양식을 불러 옵니다.",
        html: '<span style="font-size:36px;">교육 활동 소개</span><br><p>교육 이름 : </p><br><br><p>교육 주최기관 : </p><br><br><p>교육 기간 : </p><br><br><hr><br><br><span style="font-size:36px;">주요 교육 내용</span><br><br><p>느낀 점 : </p><br><br><p>증빙 자료 : </p><br><br>'
    }, {
        title: "공모전", image: "contest.png", description: "공모전에 관한 양식을 불러 옵니다.",
        html: '<span style="font-size:36px;">공모전 활동 소개</span><br><p>공모전 이름 : </p><br><br><p>공모전 주최 기간:</p><br><br><hr><br><br><span style="font-size:36px;">활동 내용</span><br><br><p>팀명 및 나의 역할 : </p><br><br><p>작품 설명 : </p><br><br><p>작품 사진 : (첨부)</p><br><br><p>느낀 점 : </p><br><br><p>수상 결과 사진 : </p><br><br>'
    }]
});