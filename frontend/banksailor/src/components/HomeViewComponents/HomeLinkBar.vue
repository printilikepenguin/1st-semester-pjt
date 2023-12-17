<template>
  <div class="middle-bar">
    <div class="middle-bar-item" style="margin-left: 20px;">
      <a href="https://www.youtube.com/">
        <img src="@/assets/Homeview/youtube_icon.png" alt="" width="40" class="middle-bar-icon">
      </a>
      <div class="middle-bar-place">
        <div class="place-title">Youtube</div>
        <div class="place-description">각종 금융 정보를 뱅크세일러<br>유튜브를 통해 확인하세요</div>
      </div>
    </div>
    <div class="middle-bar-item">
      <a href="https://www.instagram.com/">
        <img src="@/assets/Homeview/instagram_icon.png" alt="" width="40" class="middle-bar-icon">
      </a>
      <div class="middle-bar-place">
        <div class="place-title">Instagram</div>
        <div class="place-description">뱅크세일러 이벤트 및 공지를<br>인스타그램을 통해 확인하세요</div>
      </div>
    </div>
    <div class="middle-bar-item">
      <a href="https://www.fss.or.kr/">
        <img src="@/assets/Homeview/finance_icon.png" alt="" width="40" class="middle-bar-icon">
      </a>
      <div class="middle-bar-place">
        <div class="place-title">금융감독원</div>
        <div class="place-description">금융상품과 관련한<br>공시를 확인하실 수 있습니다</div>
      </div>
    </div>
    <div class="middle-bar-item">
      <a href="https://www.nts.go.kr/">
        <img src="@/assets/Homeview/tax_icon.png" alt="" width="40" class="middle-bar-icon">
      </a>
      <div class="middle-bar-place">
        <div class="place-title">국세청</div>
        <div class="place-description">금융상품 이자의 과세정보를<br>확인하실 수 있습니다</div>
      </div>
    </div>
    <div class="middle-bar-item" style="margin-right: 20px;">
      <a href="https://www.moef.go.kr/">
        <img src="@/assets/Homeview/government_icon.png" alt="" width="40" class="middle-bar-icon">
      </a>
      <div class="middle-bar-place">
        <div class="place-title">기획재정부</div>
        <div class="place-description">각종 금융관련 공시 및 정책을<br>확인하실 수 있습니다</div>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.middle-bar {
  width: 80%;
  height: 100px;
  box-shadow: 5px 5px 15px 5px lightgray;
  border-radius: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  column-gap: 20px;
}

.middle-bar-item {
  width: 20%;
  display: flex;
  align-items: center;
  justify-content: center;
  column-gap: 10px;
}

.middle-bar-place {
  display: flex;
  flex-direction: column;
  row-gap: 3px;
}


.place-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 500;
}


.place-description{
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 0.8rem;
}
</style>